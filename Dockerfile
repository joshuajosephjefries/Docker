ARG VERSION=latest
FROM amazonlinux:${VERSION}
ENV container docker
# MAINTAINER bjosephjefries@gmail.com -> Depreciated
RUN yum install -y git
CMD git --version
LABEL description="Git VCS Installation"
