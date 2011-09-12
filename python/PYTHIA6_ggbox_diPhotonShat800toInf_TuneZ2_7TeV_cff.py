import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2Settings_cfi import *

generator = cms.EDFilter("Pythia6GeneratorFilter",   
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(7000.0),
    maxEventsToPrint = cms.untracked.int32(0),
    crossSection  = cms.untracked.double(1.234e-4),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring(
            'MSEL=0 ',
            'MSUB(114)=1       ',
            'CKIN(1)=800.          ! minimum s hat for hard interactions', 
            'CKIN(2)=-1.          ! maximum s hat for hard interactions'),

        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    name = cms.untracked.string('$Source: /cvs/CMSSW/CMSSW/Configuration/GenProduction/python/PYTHIA6_ggbox_diPhotonPt10to25_TuneZ2_7TeV_cff.py,v $'),
    annotation = cms.untracked.string('PYTHIA6 gg to diphotons box with Pt10-25 at sqrt(s) = 7TeV')
)
ProductionFilterSequence = cms.Sequence(generator)


