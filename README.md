# Tooling plugathon
## 1 Introduction
### 1.1 General introduction

EHDS requirements regarding the FHIR implementations are published in the form of FHIR profiles. Profiles are a mechanism to describe, in a structured way, what the requirements are, and to automatically validate if a resource (a FHIR instance) actually conforms to the stated requirements.

The plugathon is aimed at producing FHIR resources that conform to the EHDS profiles. As such, profile validation plays an important role.

There are many tools available for FHIR validation (see [here](https://confluence.hl7.org/spaces/FHIR/pages/35718864/Profile+Tooling) and [here](https://confluence.hl7.org/spaces/FHIR/pages/35718869/Testing+Platforms)). For those who aren't experienced with using such tools, we prepared a tool setup based on the IG Publisher by HL7.

### 1.2 Requirements

* A laptop with the software needed for developing your application
* Either
    * Your own FHIR validation tools; or
    * A Github account (not an enterprise account, see below) with permissions to fork a public repository, plus a git client to sync your laptop with it; or
    * Docker Desktop or compatible software installed on your laptop (see below).
* Basic knowledge on using the command line.
* Recommended: an account on the Nationale Terminologieserver, with additional access to SNOMED and LOINC. See the manual [in English](https://nictiz.nl/publicaties/national-terminology-server-manual-for-new-users/) or [Dutch](https://nictiz.nl/publicaties/nationale-terminologie-server-handleiding-voor-nieuwe-gebruikers/).

### 1.3 European specifications

This tool set has the following European specifications pre-loaded:

* [Europe Patient Summary](https://build.fhir.org/ig/hl7-eu/eps/)
* [Europe Medication Prescription and Dispense](https://hl7.eu/fhir/mpd/)
* [Europe Base and Core FHIR](https://hl7.eu/fhir/base/)
* [Europe Laboratory Report](https://hl7.eu/fhir/laboratory/)
* [Europe Hospital Discharge Report](https://hl7.eu/fhir/hdr/)
* [Europe Base and Core FHIR IG](https://hl7.eu/fhir/base/)

An overview of the various HL7 Europe specifications can be found here: https://hl7.eu/fhir/

For a detailed overview see: [The European Patient Summary](eps.MD).

## 2 Using the validation tooling

There are two options:

1. Using a Github Codespace:
    * The IG Publisher tool runs on the Github servers in the cloud.
    * FHIR instances you want to test are exported as files and checked in to this repository.
    * Requirements: you need to be able to create a repository on Github and have a git client on your computer. No additional software is needed.
    * Optionally: an account on the Nationale Terminologieserver to check Dutch terms.
2. Using a local Docker container:
    * The IG Publisher runs in a Docker container on your computer.
    * FHIR instances you want to test are exported as files.
    * Requirements: Docker Desktop or similar on your computer (Docker Desktop is recommended if you have little prior experience with containers). No additional software is needed.
    * Optionally: an account on the Nationale Terminologieserver to check Dutch terms.

### 2.1 Github Codespace

To use the Github Codespace option, you need to be able to create a git repository on Github and be able to synchronize with it.

* Each Github user has a monthly quotum for the use of codespaces. The free tier (120 hours) is more than sufficient for the plugathon. Please be aware that more usage can result in billing for the Github user.
* Enterprise accounts [cannot be used](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces#free-quota).
* If the repository for the plugathon will be hosted in a payed organization account, the use of codespaces [needs to be enabled for the plugathon](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/enabling-or-disabling-github-codespaces-for-your-organization#enabling-or-disabling-github-codespaces).

To use:

1. Fork the repository at <https://github.com/Nictiz/Plugathon-Validator> using the "fork" button in the upper right corner. *Note*: forking is not the same as cloning, [see the documentation](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo).
2. Synchronize this fork to your computer using your favorite git client.
3. Go to the Github page for your repository and find the green "Code" button. Click it and select the "Codespaces" tab. Click the "+" button.<br>The codespace is now being set up for the first time. This will take quite a bit of time as all the required tooling is installed. Subsequent runs will be faster.
4. After some time, you will have Visual Studio Code running in your browser. On the left side you'll see the folder structure from your repository. If you want, you can open files here for editing. You also have access to a git client here to pull changes from your local computer.
5. In the lower half you'll also see a terminal window. From here on, continue with [the section on using the tool](#Using-the-tool).

### 2.2 Local Docker container

This option bundles all required software in a lightweight virtual machine that can be run from your computer. To use it, you need to have an engine that can run Docker containers.

* If you're not familiar with Docker containers, Docker Desktop is the easiest option. Installation may require special permissions on your computer.
* As an alternative, Podman Desktop can be used.
* If you know what you're doing, a bare-bones container engine without desktop GUI can be used.

To use:
1. Clone the repository at <https://github.com/Nictiz/Plugathon-Validator> to your computer.
2. Run the script `init-container.bat` or `init-container.sh`/<br>The image will now be built. This will take quite a bit of time as all the required tooling is installed. It only needs to be done once.
3. When done, run the `start-container.bat` or `start-container.sh` script.
4. From here on, continue with [the section on using the tool](#Using-the-tool).

### 2.3 Using the tool

To access the tool, first start a local Docker container or a Github Codespace. Once you started one of these options, you're in a Linux terminal environment. The validation tooling will be run from this environment. The resulting QA report is presented in the web browser.

This environment is based on the HL7 IG Publisher in combination with the Nationale Terminologieserver (it deviates slightly from a standard IG Publishing environment to facilitate profile matching and using the NTS).

1. To validate resources, create a "resources" subfolder of the "input" folder and place resources here.
    * Resources ideally contain a `Resource.id` as this is needed for the IG Publishing process. If this is missing, a `Resource.id` will be added.
    * Resources will automatically be matched to the relevant EHDR profiles. If desired, they may state their profile conformance in the `Resource.meta.profile` tag, but this is optional.
2. When using the Github Codespace option, commit these resources to your repository and push the commit to Github. From the Codespace, run `git pull` after each check in. (The local Docker container picks up whatever is in the folder).
3. To start the IG Publisher, simply run the `go [core|eps|medication|lab|hdr]` command (choose whichever is applicable). The options mean:
    * `core` to validate against the eu-core profiles.
    * `eps` to validate against the European Patient Summary profiles.
    * `medication` to validate against the ePrescription/eDispensation profiles.
    * `lab` to match against the Laboratory Results profiles.
    * `hdr` to match against the Hospital Discharge Report profiles.
4. On the first run, the tool will ask if you want to use the Nationale Terminologieserver (NTS), and if so, what your username and password are. If you don't use the NTS, the default FHIR terminology server will be used.<p>WARNING: your username and password will be stored in plaintext in the container!
5. Building the IG takes some time.
6. When the build has finished:
    * When using the Codespace, run `show` to serve the created IG. A popup will appear allowing you to open the result in your browser. From here, you can navigate to the QA page.
    * When using the local Docker container, you can run `show` and navigate to <http://localhost:4000>. Alternatively, you can double click the "qa.html" page in the "output" folder on your computer.
    * Press Ctrl + C to stop serving the IG.
7. To re-validate, put the changed resources in the "resources" subfolder and repeat these steps.

### 2.5 Using the Nationale Terminologieserver

By default, the IG Publisher uses the publicly available `tx.fhir.org` terminology server for validation. This server offers limited support for Dutch translations (and is a bit unstable). As an alternative, the Nationale Terminologieserver may be used. However, this server requires a user account, and in addition, requires that the available code systems are accessible to that account. See https://nictiz.nl/wat-we-doen/activiteiten/terminologie/de-nationale-terminologieserver/ for more information.

When the tool is run for the first time, it will ask you for credentials for the Nationale Terminologieserver. Subsequent runs will re-use the choice you made here. If you want to change this, you can run the `tx` command.

## 3 FAQ
### 3.1 How do I add resources to validate?
All resources to validate should be placed in the folder "input/resources".

If you're using a local Docker installation, you can simply put them there and run the `go` command.

If you're using a codespace, there are multiple ways:
* The easiest way is to drag-and-drop resource from you development computer to the folder in your codespace.
* Alternatively, you may use the built-in git client to synchronize from checked-in files. Please be aware that the codespace acts as just another client; to load files in your codespace, you would need to push from you local computer to Github first, and then pull from Github to your codespace.

### 3.2 Do I need to state the profile to use in `Resource.meta.profile`?
It is not necessary to state the profile to validate against in your resources. When running the `go` command, a script is executed to match resources to the relevant profiles for the specified IG.

FHIR profiles are used to define the rules and restrictions for a resource in a particular use case. As a resource may be usable in several distinct use cases, there is no tight binding between a resource and a profile, so it's normally not necessary for a resource to indicate the profile or profiles it conforms to.

If you want, you may specify (all the) profile(s) your resources conform to using the `Resource.meta.profile` tag as a hint to validation tooling. If this tag is present, the IG Publisher will pick it up.

### 3.3 Why does the tool change my resource?
For the IG Publisher to work properly, a `Resource.id` is necessary in each resource to check. For this reason it will be added if it is absent.

Please note that in most use cases, adding a `Resource.id` is required.

### 3.4 Can I add extra package dependencies?
The tooling will set package dependencies for the use case chosen using het `go` command. For example, if use case `eps` is chosen, the package dependency on the European Patient Summary IG will be set.

If your FHIR instances have additional dependencies, you can add them to the file "input/IG.json", using the `dependsOn` key.

For example, to add a dependency on the nl-core package, expand `dependsOn` to:

```json
    "dependsOn": [
        {
            "uri": "http://nictiz.nl/fhir",
            "packageId": "nictiz.fhir.nl.r4.nl-core",
            "version": "0.12.0-beta.4"
        }
    ],
```

### 3.5 Can I suppress warnings and errors?
The IG Publisher has an option to [suppress messages in the QA report](https://confluence.hl7.org/spaces/FHIR/pages/66938614/Implementation+Guide+Parameters#ImplementationGuideParameters-ManagingWarningsandHints). This is useful for errors and warnings that cannot be fixed at the moment and can help you to focus on the messages that are actually relevant.

To do so, open the file "input/ignoreWarnings.txt". Messages to be suppressed are grouped using header line, which starts by a `#` and describes the reason to suppress the message. Beneath this line, add the messages to suppress. The "%" wildcard can be used at the start and end of a line.

### 3.6 When using the Nationale Terminologieserver, why do I get a message that no terminology server is used?
This seems to happen sometimes on the first run, it's a bug in our tool setup. Please re-run the `go` command.

### 3.7 Can I switch between the default terminology server and the Nationale Terminologieserver?
You can setup you terminology server preferences using the `tx` command. However, the IG Publisher caches terminology server calls between runs. When switching, you might want to delete the "input-cache/txcache" folder.

### 3.8 Can I save QA reports?
The IG Publisher generates QA reports in different formats in the "output" folder:

* qa.html -- human readable version.
* qa.txt -- human readable version in flat text.
* qa.xml -- machine readable version in OperationOutcome format.

If you want to keep these reports for later reference, you can simple save the files you're interested in (for the HTML version, it might be a good idea to save it as a "complete web page" from your browser to include all images etc.).

You can also leverage git to commit the QA reports together with the input resources. To do so, open the ".gitignore" file and uncomment the relevant line(s) to include the QA reports in git.

### 3.9 How can I change the language to use for resource checking?
The IG Publisher will try to determine the language for each resource based on the the [`Resource.language` tag](https://www.hl7.org/fhir/R4/resource-definitions.html#Resource.language) and the default language specified using the `i18n-default-lang` parameter indicated in "IG.json" (currently set to _nl-NL_).

### 3.10 Can I still use this tool when the plugathon is over?
This repo is a simple wrapper around the [FHIR IG Publisher]((https://confluence.hl7.org/spaces/FHIR/pages/35718627/IG+Publisher+Documentation)), which is very actively maintained by HL7. The IG Publisher can be a bit overwhelming to set up, so we created this wrapper for the single purpose to quickly start validating using the EHDS specs. It will still be available after the plugathon, but there are no plans to actively maintain it.

Please note that there are many ways to do profile validation in FHIR, which might better suit your purpose. Options include:

- Software libraries which allow you to build in profile validation in your application.
- Command line tools which can be used stand-alone or built into a development pipeline.
- FHIR servers can perform profile validation when asked to.
- FHIR specific development platforms that offer this functionality out of the box.

HL7 [maintains a Confluence page](https://confluence.hl7.org/spaces/FHIR/pages/35718864/Profile+Tooling) with pointers to implementations. Also see [this ticket](https://nictiz.atlassian.net/browse/MM-1690). 