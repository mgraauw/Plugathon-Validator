import json
import uuid
import xml.etree.ElementTree as ET

from pathlib import Path

FHIR_NS = "http://hl7.org/fhir"
NS = {"f": FHIR_NS}
ET.register_namespace("", FHIR_NS)

IG_DIR = Path("/ig/")

def openResource(file_path):
    resource = None
    if len(file_path.suffixes) and file_path.suffixes[-1].lower() == ".xml":
        tree = ET.parse(file_path)
        resource = tree.getroot()
    elif len(file_path.suffixes) and file_path.suffixes[-1].lower() == ".json":
        with open(file_path) as f:
            resource = json.load(f)
    else:
        print(f"Not a FHIR resource: {file_path}. Skipping")

    return resource

def getResourceId(resource):
    try:
        if isinstance(resource, ET.Element):
            id = resource.find("f:id", NS).attrib["value"]
        elif isinstance(resource, dict):
            id = resource["id"]
    except (KeyError, AttributeError):
        return None

    return id

def addResourceId(resource, file_path):
    new_id = str(uuid.uuid4())

    if isinstance(resource, ET.Element):
        id_el = ET.Element("id")
        id_el.set("value", new_id)
        resource.insert(0, id_el)
        et = ET.ElementTree(resource)
        et.write(file_path)
    elif isinstance(resource, dict):
        resource["id"] = new_id
        with open(file_path, "w") as f:
            f.write(json.dumps(resource, indent=4))

def getResourceType(resource):
    if isinstance(resource, ET.Element):
        return resource.tag.replace("{" + FHIR_NS + "}", "")
    elif isinstance(resource, dict):
        if "resourceType" in resource:
            return resource["resourceType"]
        else:
            raise Error("JSON resource misses the 'resourceType' key")


def mapToProfile(resource):
    resource_type = getResourceType(resource)

    if resource_type == "Patient":
        return "http://hl7.eu/fhir/eps/StructureDefinition/patient-eu-eps"
    elif resource_type == "Procedure":
        return "http://hl7.eu/fhir/eps/StructureDefinition/procedure-eu-eps"

    return None

if __name__ == "__main__":
    resources = []

    resource_type = None
    profile = None
    resource_id = None

    for file_path in IG_DIR.glob("input/resources/*"):
        if resource := openResource(file_path):
            resource_id = getResourceId(resource)
            if not resource_id:
                print(f"Resource is missing an id, so it's added for file: {file_path}")
                addResourceId(resource, file_path)
                resource = openResource(file_path)

            resource_type = None
            try:
                resource_type = getResourceType(resource)
            except Error as e:
                print(f"Problem parsing resource: {file_path} ({e}). Skipping")
            profile = mapToProfile(resource)
            if not profile:
                print(f"No profile could be matched to resource: {file_path}. Skipping")
            

            if resource_type and profile and resource_id:
                resources.append({
                    "reference": {
                        "reference": f"{resource_type}/{resource_id}"
                    },
                    "exampleCanonical": profile
                })

    with open(IG_DIR / "input/IG.json") as f:
        base_ig = json.load(f)
    with open(IG_DIR / "IG_generated.json", "w") as f:
        base_ig["definition"]["resource"] = resources
        f.write(json.dumps(base_ig, sort_keys=False, indent=4))

    ini_path = IG_DIR / "ig.ini"
    if not ini_path.exists():
        with open(ini_path, "w") as f:
            f.write("[IG]\n")
            f.write("ig = IG_generated.json\n")
            f.write("template = fhir.base.template#current\n")