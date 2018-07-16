from htt_plot.tools.cut import Cut

pt1=23.
eta1=2.1
iso1=0.15
pt2=30.
eta2=2.3
iso2=1. #1.5

mt_cut_value = 70.

cut_flags = Cut('Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_goodVertices && Flag_eeBadScFilter && Flag_globalTightHalo2016Filter && passBadMuonFilter && passBadChargedHadronFilter && badMuonMoriond2017 && badCloneMuonMoriond2017')

cut_vetoes = Cut('!veto_dilepton && !veto_thirdlepton && !veto_otherlepton')

cut_tau_kinematics = Cut('l2_pt>{pt2} && abs(l2_eta)<{eta2}'.format(pt2=pt2,eta2=eta2))
cut_tau_vertex = Cut('abs(l2_dz)<0.2')
cut_tau_ID = Cut('l2_decayModeFinding>0.5 && l2_againstElectronMVA6>0.5 && l2_againstMuon3>1.5')
cut_tau_iso = Cut('l2_byIsolationMVArun2v1DBoldDMwLT>3.5')

cut_mu_kinematics = Cut('l1_pt>{pt1} && abs(l1_eta)<{eta1}'.format(pt1=pt1,eta1=eta1))
cut_mu_vertex = Cut('abs(l1_dxy)<0.045 && abs(l1_dz)<0.2')
cut_mu_ID = Cut('l1_muonid_medium>0.5')
cut_mu_iso = Cut('l1_reliso05<{iso1}'.format(iso1=iso1))

cut_ztt = Cut('gen_match_2==5')

cut_zl = Cut('gen_match_2<5')

cut_zj = Cut('gen_match_2==6')

cut_OS = Cut('l1_charge != l2_charge')
cut_SS = ~cut_OS

cut_iso_QCD_A = Cut('l2_byIsolationMVArun2v1DBoldDMwLT>2.5')
cut_iso_QCD_max = Cut('l2_byIsolationMVArun2v1DBoldDMwLT>0.5')
cut_iso_QCD_C = ~cut_iso_QCD_A & cut_iso_QCD_max
cut_iso_QCD_D = cut_iso_QCD_C

cut_QCD_A = cut_iso_QCD_A & cut_SS
cut_QCD_C = cut_iso_QCD_C & cut_OS
cut_QCD_D = cut_iso_QCD_D & cut_SS