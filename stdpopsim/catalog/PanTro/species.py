import stdpopsim

from . import genome_data

_kuderna2017 = stdpopsim.Citation(
    doi="https://doi.org/10.1093/gigascience/gix098",
    year=2017,
    author="Kuderna et al.",
    reasons={stdpopsim.CiteReason.ASSEMBLY},
)

_kong2012 = stdpopsim.Citation(
    doi="https://doi.org/10.1038/nature11396",
    year=2012,
    author="Kong et al.",
    reasons={stdpopsim.CiteReason.MUT_RATE},
)

_stevison2015 = stdpopsim.Citation(
    doi="https://doi.org/10.1093/molbev/msv331",
    year=2015,
    author="Stevison et al.",
    reasons={stdpopsim.CiteReason.REC_RATE},
)

_langergraber2012 = stdpopsim.Citation(
    doi="https://doi.org/10.1073/pnas.1211740109",
    year=2012,
    author="Langergraber et al.",
    reasons={stdpopsim.CiteReason.GEN_TIME},
)

_deManuel2016 = stdpopsim.Citation(
    doi="https://doi.org/10.1126/science.aag2602",
    year=2016,
    author="de Manuel et al.",
    reasons={stdpopsim.CiteReason.POP_SIZE},
)

_chromosomes = []
for name, data in genome_data.data["chromosomes"].items():
    _chromosomes.append(
        stdpopsim.Chromosome(
            id=name,
            length=data["length"],
            synonyms=data["synonyms"],
            mutation_rate=1.2e-8,
            recombination_rate=0.7e-8,
        )
    )

_genome = stdpopsim.Genome(
    chromosomes=_chromosomes,
    assembly_name=genome_data.data["assembly_name"],
    assembly_accession=genome_data.data["assembly_accession"],
    citations=[
        _kuderna2017.because(stdpopsim.CiteReason.ASSEMBLY),
        _kong2012.because(stdpopsim.CiteReason.MUT_RATE),
        _stevison2015.because(stdpopsim.CiteReason.REC_RATE),
    ],
)
stdpopsim.utils.append_common_synonyms(_genome)

_species = stdpopsim.Species(
    id="PanTro",
    ensembl_id="pan_troglodytes",
    name="Pan troglodytes",
    common_name="Chimpanzee",
    genome=_genome,
    generation_time=25.0,
    population_size=15000,
    citations=[
        _langergraber2012.because(stdpopsim.CiteReason.GEN_TIME),
        _deManuel2016.because(stdpopsim.CiteReason.POP_SIZE),
    ],
)

stdpopsim.register_species(_species)
