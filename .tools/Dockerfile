FROM mcr.microsoft.com/devcontainers/java:21-bookworm

# Install system components
RUN apt-get update && apt-get -y install build-essential jq nodejs npm ruby-full rubygems zlib1g-dev mitmproxy python3-requests python3-termcolor wget dos2unix

# Install Jekyll
RUN gem install bundler jekyll

# Add mitmproxy certificate
RUN su - vscode -c mitmdump & sleep 2
RUN cp -r /home/vscode/.mitmproxy /root && chown -R root:root /root/.mitmproxy
RUN keytool -noprompt -importcert -alias mitmproxy -storepass changeit -keystore $JAVA_HOME/lib/security/cacerts -trustcacerts -file ~/.mitmproxy/mitmproxy-ca-cert.pem

# Create the needed packages folder
RUN mkdir -p /root/.fhir/packages

# Create the mount point and make it a trusted to git
RUN mkdir /ig
RUN git config --global --add safe.directory /ig

# Install our tools
RUN mkdir /tools
RUN wget https://raw.githubusercontent.com/Nictiz/snippets/refs/heads/main/NTS-proxy/NTS-proxy.py -O /tools/NTS-proxy.py
RUN wget https://github.com/HL7/fhir-ig-publisher/releases/latest/download/publisher.jar -O /tools/publisher.jar
COPY createIG.py /tools
COPY go /tools
COPY show /tools
COPY tx /tools
RUN dos2unix /tools/go
RUN dos2unix /tools/show
RUN dos2unix /tools/tx
RUN chmod 755 /tools/go
RUN chmod 755 /tools/show
RUN chmod 755 /tools/tx

# EU profiles are not published to the package repository's, so we'll have get them manually
RUN mkdir -p /var/lib/.fhir/packages
RUN mkdir /var/lib/.fhir/packages/hl7.fhir.eu.eps#0.0.1-ci && wget -O - https://build.fhir.org/ig/hl7-eu/eps/package.tgz | tar -xz -C /var/lib/.fhir/packages/hl7.fhir.eu.eps#0.0.1-ci
RUN mkdir /var/lib/.fhir/packages/hl7.fhir.eu.hdr#current && wget -O - https://hl7.eu/fhir/hdr/package.tgz | tar -xz -C /var/lib/.fhir/packages/hl7.fhir.eu.hdr#current

RUN echo 'echo "Welcome to the Plugathon Validator container"' >> /etc/bash.bashrc
RUN echo 'echo' >> /etc/bash.bashrc
RUN echo 'echo "This container uses the IG Publisher as a tool for validation of resources. To use:"' >> /etc/bash.bashrc
RUN echo 'echo "* place resources in the \"input/resources\" folder"' >> /etc/bash.bashrc
RUN echo 'echo "* generate the IG using the \"go [core|eps|medication|lab|hdr]\" command (choose the IG you want to test for)"' >> /etc/bash.bashrc
RUN echo 'echo "* consult the QA page of the IG using the \"show\" command"' >> /etc/bash.bashrc
RUN echo 'echo' >> /etc/bash.bashrc
RUN echo 'echo "Resources should be in XML or JSON format and should ideally contain a Resource.id (if not, one will be added)."' >> /etc/bash.bashrc
RUN echo 'echo "Resources will be checked against the relevant EHDS FHIR profiles from the IG chosen with the \"go\". It is not needed to set a profile declaration using meta.profile."' >> /etc/bash.bashrc
RUN echo 'echo' >> /etc/bash.bashrc
RUN echo 'echo "The IG Publisher can use the Nationale Terminologieserver (NTS) instead of the default FHIR terminology server if you have a login. The \"go\" command will ask you for credentials on the first run (you can always change the configuration using the \"tx\" command)."' >> /etc/bash.bashrc
RUN echo 'echo' >> /etc/bash.bashrc
RUN echo 'echo "WARNING: If you provide a password for the NTS, it will be stored in plaintext in this container!!"' >> /etc/bash.bashrc

ENV PATH="/tools:${PATH}"
ENTRYPOINT /bin/bash