FROM mcr.microsoft.com/devcontainers/java:21

# Install system components
RUN apt-get update && apt-get -y install build-essential jq nodejs npm ruby-full rubygems zlib1g-dev mitmproxy python3-requests wget

# Install Jekyll
RUN gem install bundler jekyll

# Get our tools
RUN mkdir /tools
RUN wget https://raw.githubusercontent.com/Nictiz/snippets/refs/heads/main/NTS-proxy/NTS-proxy.py -O /tools/NTS-proxy.py
COPY createIG.py /tools
RUN wget https://github.com/HL7/fhir-ig-publisher/releases/latest/download/publisher.jar -O /tools/publisher.jar

# Add mitmproxy certificate
RUN mitmdump & sleep 2 && keytool -noprompt -importcert -alias mitmproxy -storepass changeit -keystore $JAVA_HOME/lib/security/cacerts -trustcacerts -file ~/.mitmproxy/mitmproxy-ca-cert.pem

ENV PATH="${PATH}:/usr/local/lib"

# Create the needed packages folder
RUN mkdir -p /root/.fhir/packages

# Create the mount point and make it a trusted to git
RUN mkdir /ig
RUN git config --global --add safe.directory /ig
COPY go /tools
RUN chmod 755 /tools/go
COPY ig.ini /ig

ENV PATH="/tools:${PATH}"
WORKDIR "/ig"
ENTRYPOINT /bin/bash