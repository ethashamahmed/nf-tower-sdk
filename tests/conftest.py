"""Unit test config."""

import os

import pytest

from nf_tower_sdk.clients import AuthenticatedClient, ComputeEnvs
from nf_tower_sdk.nft.api_library.models import (
    ComputeEnv,
    CreateComputeEnvRequest,
    IBMLSFConfiguration,
)
from nf_tower_sdk.tower import NextflowTowerClient


@pytest.fixture
def tower_client() -> NextflowTowerClient:
    "Nextflow Tower client for testing."
    return NextflowTowerClient(
        url="https://tower.nf",
        api_token=os.getenv("NFT_API_TOKEN"),
    )


@pytest.fixture
def test_client() -> AuthenticatedClient:
    "Nextflow Tower client for testing."
    return AuthenticatedClient(
        base_url="https://tower.nf/api",
        token=os.getenv("NFT_API_TOKEN"),
    )


# pylint: disable=redefined-outer-name
@pytest.fixture
def compute_env_client(test_client: AuthenticatedClient) -> ComputeEnvs:
    "ComputeEnvs client for testing."
    return ComputeEnvs(test_client)


@pytest.fixture
def test_compute_env() -> dict:
    "Compute env details for testing."
    return {"name": "AWS_Batch_Ireland", "id": "2DViEIDMdMDXE0B2VTpsa0"}


@pytest.fixture
def compute_env_request() -> CreateComputeEnvRequest:
    "Compute env request object for testing."
    return CreateComputeEnvRequest(
        compute_env=ComputeEnv(
            name="Test", config=IBMLSFConfiguration()
        )
    )


@pytest.fixture
def test_org() -> dict:
    "Tower organisation details for testing."
    return {"name": "community", "id": 187965850823746}


@pytest.fixture
def test_workspace() -> dict:
    "Tower workspace details for testing."
    return {"name": "showcase", "id": 40230138858677}


@pytest.fixture
def test_workflow() -> dict:
    "Details of workflow to use for testing."
    return {
        "name": "nf-core-rnaseq",
        "pipeline_id": 175099328146358,
        "workflow_id": "2ZTGegpXyjPF3U",
        # pylint: disable=line-too-long
        "params": {
            "help": False,
            "gff": "https://github.com/nf-core/test-datasets/raw/rnaseq/reference/genes.gff.gz",
            "skip_qc": False,
            "rseqc_modules": "bam_stat,inner_distance,infer_experiment,junction_annotation,junction_saturation,read_distribution,read_duplication,tin",
            "fasta": "https://github.com/nf-core/test-datasets/raw/rnaseq/reference/genome.fa",
            "save_unaligned": False,
            "skip_bigwig": False,
            "max_cpus": 2,
            "featurecounts_feature_type": "exon",
            "with_umi": False,
            "save_bbsplit_reads": False,
            "skip_qualimap": False,
            "config_profile_description": "Minimal test dataset to check pipeline function",
            "skip_alignment": False,
            "save_trimmed": False,
            "show_hidden_params": False,
            "skip_markduplicates": False,
            "schema_ignore_params": "genomes",
            "skip_multiqc": False,
            "max_time": "3.h",
            "bbsplit_fasta_list": "https://github.com/nf-core/test-datasets/raw/rnaseq/reference/bbsplit_fasta_list.txt",
            "gtf_extra_attributes": "gene_name",
            "save_merged_fastq": False,
            "salmon_index": "https://github.com/nf-core/test-datasets/raw/rnaseq/reference/salmon.tar.gz",
            "input": "https://api.tower.nf/workspaces/40230138858677/datasets/66XmaViCT87OV8aGYS2Pk1/v/1/n/samplesheet_test.csv",
            "skip_preseq": False,
            "skip_rseqc": False,
            "hisat2_build_memory": "200.GB",
            "skip_bbsplit": False,
            "gtf_group_features": "gene_id",
            "stringtie_ignore_gtf": False,
            "skip_deseq2_qc": False,
            "validate_params": True,
            "save_umi_intermeds": False,
            "deseq2_vst": False,
            "bam_csi_index": False,
            "umitools_bc_pattern": "NNNN",
            "save_align_intermeds": False,
            "skip_fastqc": False,
            "gtf": "https://github.com/nf-core/test-datasets/raw/rnaseq/reference/genes.gtf.gz",
            "pseudo_aligner": "salmon",
            "skip_biotype_qc": False,
            "rsem_index": "https://github.com/nf-core/test-datasets/raw/rnaseq/reference/rsem.tar.gz",
            "max_memory": "6.GB",
            "skip_dupradar": False,
            "hisat2_index": "https://github.com/nf-core/test-datasets/raw/rnaseq/reference/hisat2.tar.gz",
            "save_reference": False,
            "skip_trimming": False,
            "ribo_database_manifest": "${projectDir}/assets/rrna-db-defaults.txt",
            "remove_ribo_rna": False,
            "igenomes_ignore": False,
            "custom_config_version": "master",
            "aligner": "star_salmon",
            "outdir": "",
            "min_mapped_reads": 5,
            "enable_conda": False,
            "featurecounts_group_type": "gene_biotype",
            "transcript_fasta": "https://github.com/nf-core/test-datasets/raw/rnaseq/reference/transcriptome.fasta",
            "igenomes_base": "s3://ngi-igenomes/igenomes",
            "max_multiqc_email_size": "25.MB",
            "save_non_ribo_reads": False,
            "config_profile_name": "Test profile",
            "skip_stringtie": False,
            "gencode": False,
            "star_ignore_sjdbgtf": False,
            "plaintext_email": False,
            "star_index": "https://github.com/nf-core/test-datasets/raw/rnaseq/reference/star.tar.gz",
            "umitools_extract_method": "string",
            "additional_fasta": "https://github.com/nf-core/test-datasets/raw/rnaseq/reference/gfp.fa.gz",
            "monochrome_logs": False,
            "custom_config_base": "https://raw.githubusercontent.com/nf-core/configs/master",
            "tracedir": "${params.outdir}/pipeline_info",
        },
    }
