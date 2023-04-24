from enum import Enum


class CredentialsProvider(str, Enum):
    AWS = "aws"
    AZURE = "azure"
    BITBUCKET = "bitbucket"
    CODECOMMIT = "codecommit"
    CONTAINER_REG = "container-reg"
    GITHUB = "github"
    GITLAB = "gitlab"
    GOOGLE = "google"
    K8S = "k8s"
    SSH = "ssh"
    TW_AGENT = "tw-agent"

    def __str__(self) -> str:
        return str(self.value)
