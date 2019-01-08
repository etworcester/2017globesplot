#!/usr/bin/env python

import sys
import math
import ROOT
from array import array

ROOT.gROOT.SetStyle("Plain")
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptFit()
ROOT.gStyle.SetCanvasColor(0)
ROOT.gStyle.SetTitleFillColor(0)
ROOT.gStyle.SetTitleBorderSize(0)
ROOT.gStyle.SetFrameBorderMode(0)
ROOT.gStyle.SetMarkerStyle(20)
ROOT.gStyle.SetTitleX(0.5)
ROOT.gStyle.SetTitleAlign(23)
ROOT.gStyle.SetLineWidth(3)
ROOT.gStyle.SetLineColor(1)
ROOT.gStyle.SetTitleSize(0.03,"t")

def filldiff(up,down):
      n = up.GetN()
      diffgraph = ROOT.TGraph(2*n);
      i = 0
      xup = ROOT.Double(-9.9)
      yup = ROOT.Double(-9.9)
      xlo = ROOT.Double(-9.9)
      ylo = ROOT.Double(-9.9)
      while i<n:
          up.GetPoint(i,xup,yup);
          down.GetPoint(n-i-1,xlo,ylo);
          diffgraph.SetPoint(i,xup,yup);
          diffgraph.SetPoint(n+i,xlo,ylo);
          i += 1
      return diffgraph;

explist = [0,1,5,10,28,50,100,200,300,400,556,600,800,984,1000,1250,1500]
cpvlist75_ref_short = [0]
cpvlist50_ref_short = [0]
cpvlistbest_ref_short = [0]
mhlist_ref_short = [0]
mhlistbest_ref_short = [0]
cpvlist75_ref_short_3pc = [0]
cpvlist50_ref_short_3pc = [0]
cpvlistbest_ref_short_3pc = [0]
mhlist_ref_short_3pc = [0]
mhlistbest_ref_short_3pc = [0]

cpvlist50_optimized_long = [0]
cpvlist75_optimized_long = [0]
cpvlistbest_optimized_long = [0]
mhlist_optimized_long = [0]
mhlistbest_optimized_long = [0]
cpvlist50_optimized_long_3pc = [0]
cpvlist75_optimized_long_3pc = [0]
cpvlistbest_optimized_long_3pc = [0]
mhlist_optimized_long_3pc = [0]
mhlistbest_optimized_long_3pc = [0]

for myexp in explist:

      if (myexp==0):
            continue

      #Reference: No contraints
      filename = "root/sens_optimized_long_no_noconstr_exp"+str(myexp)+".root"
      f1 = ROOT.TFile(filename)
      cpvgraph_short = f1.Get("CPVSig")
      mhgraph_short = f1.Get("MHSig")
      nvals = cpvgraph_short.GetN()
      cpv_vals = [ROOT.Double(0.0)]*nvals
      cpv_vals = array('d',cpv_vals)
      cpv_vals = cpvgraph_short.GetY()

      mh_vals = [ROOT.Double(0.0)]*nvals
      mh_vals = array('d',mh_vals)
      mh_vals = mhgraph_short.GetY()

      i = 0
      cpv_vals_short = []
      mh_vals_short = []
      while i < nvals:
            cpv_vals_short.append(cpv_vals[i])
            mh_vals_short.append(mh_vals[i])
            i += 1

      cpvsig_75_short = sorted(cpv_vals_short)[24]
      cpvsig_50_short = sorted(cpv_vals_short)[49]
      mhsig_100_short = min(mh_vals_short)
      cpvlist75_ref_short.append(cpvsig_75_short)
      cpvlist50_ref_short.append(cpvsig_50_short)
      cpvlistbest_ref_short.append(cpv_vals[26])
      mhlist_ref_short.append(mhsig_100_short)
      mhlistbest_ref_short.append(mh_vals[26])
      f1.Close()

      filename = "root/sens_optimized_long_syst3pc_no_noconstr_exp"+str(myexp)+".root"
      f1 = ROOT.TFile(filename)
      cpvgraph_short = f1.Get("CPVSig")
      mhgraph_short = f1.Get("MHSig")
      nvals = cpvgraph_short.GetN()
      cpv_vals = [ROOT.Double(0.0)]*nvals
      cpv_vals = array('d',cpv_vals)
      cpv_vals = cpvgraph_short.GetY()

      mh_vals = [ROOT.Double(0.0)]*nvals
      mh_vals = array('d',mh_vals)
      mh_vals = mhgraph_short.GetY()

      i = 0
      cpv_vals_short = []
      mh_vals_short = []
      while i < nvals:
            cpv_vals_short.append(cpv_vals[i])
            mh_vals_short.append(mh_vals[i])
            i += 1

      cpvsig_75_short_3pc = sorted(cpv_vals_short)[24]
      cpvsig_50_short_3pc = sorted(cpv_vals_short)[49]
      mhsig_100_short_3pc = min(mh_vals_short)
      cpvlist75_ref_short_3pc.append(cpvsig_75_short_3pc)
      cpvlist50_ref_short_3pc.append(cpvsig_50_short_3pc)
      cpvlistbest_ref_short_3pc.append(cpv_vals[26])
      mhlist_ref_short_3pc.append(mhsig_100_short_3pc)
      mhlistbest_ref_short_3pc.append(mh_vals[26])      
      f1.Close()

      
      #Optimized long
      filename = "root/sens_optimized_long_no_exp"+str(myexp)+".root"
      f1 = ROOT.TFile(filename)
      cpvgraph_optimized_long = f1.Get("CPVSig")
      mhgraph_optimized_long = f1.Get("MHSig")
      nvals = cpvgraph_optimized_long.GetN()
      cpv_vals = [ROOT.Double(0.0)]*nvals
      cpv_vals = array('d',cpv_vals)
      cpv_vals = cpvgraph_optimized_long.GetY()

      mh_vals = [ROOT.Double(0.0)]*nvals
      mh_vals = array('d',mh_vals)
      mh_vals = mhgraph_optimized_long.GetY()

      i = 0
      cpv_vals_optimized_long = []
      mh_vals_optimized_long = []
      while i < nvals:
            cpv_vals_optimized_long.append(cpv_vals[i])
            mh_vals_optimized_long.append(mh_vals[i])
            i += 1

      cpvsig_75_optimized_long = sorted(cpv_vals_optimized_long)[24]
      cpvsig_50_optimized_long = sorted(cpv_vals_optimized_long)[49]
      mhsig_100_optimized_long = min(mh_vals_optimized_long)
      cpvlist75_optimized_long.append(cpvsig_75_optimized_long)
      cpvlist50_optimized_long.append(cpvsig_50_optimized_long)
      cpvlistbest_optimized_long.append(cpv_vals[26])      
      mhlist_optimized_long.append(mhsig_100_optimized_long)
      mhlistbest_optimized_long.append(mh_vals[26])      
      f1.Close()

      filename = "root/sens_optimized_long_syst3pc_no_exp"+str(myexp)+".root"
      f1 = ROOT.TFile(filename)
      cpvgraph_optimized_long = f1.Get("CPVSig")
      mhgraph_optimized_long = f1.Get("MHSig")
      nvals = cpvgraph_optimized_long.GetN()
      cpv_vals = [ROOT.Double(0.0)]*nvals
      cpv_vals = array('d',cpv_vals)
      cpv_vals = cpvgraph_optimized_long.GetY()

      mh_vals = [ROOT.Double(0.0)]*nvals
      mh_vals = array('d',mh_vals)
      mh_vals = mhgraph_optimized_long.GetY()

      i = 0
      cpv_vals_optimized_long = []
      mh_vals_optimized_long = []
      while i < nvals:
            cpv_vals_optimized_long.append(cpv_vals[i])
            mh_vals_optimized_long.append(mh_vals[i])
            i += 1

      cpvsig_75_optimized_long_3pc = sorted(cpv_vals_optimized_long)[24]
      cpvsig_50_optimized_long_3pc = sorted(cpv_vals_optimized_long)[49]
      mhsig_100_optimized_long_3pc = min(mh_vals_optimized_long)
      cpvlist75_optimized_long_3pc.append(cpvsig_75_optimized_long_3pc)
      cpvlist50_optimized_long_3pc.append(cpvsig_50_optimized_long_3pc)
      cpvlistbest_optimized_long_3pc.append(cpv_vals[26])            
      mhlist_optimized_long_3pc.append(mhsig_100_optimized_long_3pc)
      mhlistbest_optimized_long_3pc.append(mh_vals[26])            
      f1.Close()

n = len(explist)
explist = array('d',explist)
cpvlist75_ref_short = array('d',cpvlist75_ref_short)
cpvlist75_optimized_long = array('d',cpvlist75_optimized_long)
cpvlist75_ref_short_3pc = array('d',cpvlist75_ref_short_3pc)
cpvlist75_optimized_long_3pc = array('d',cpvlist75_optimized_long_3pc)

cpvlist50_ref_short = array('d',cpvlist50_ref_short)
cpvlist50_optimized_long = array('d',cpvlist50_optimized_long)
cpvlist50_ref_short_3pc = array('d',cpvlist50_ref_short_3pc)
cpvlist50_optimized_long_3pc = array('d',cpvlist50_optimized_long_3pc)

cpvlistbest_ref_short = array('d',cpvlistbest_ref_short)
cpvlistbest_optimized_long = array('d',cpvlistbest_optimized_long)
cpvlistbest_ref_short_3pc = array('d',cpvlistbest_ref_short_3pc)
cpvlistbest_optimized_long_3pc = array('d',cpvlistbest_optimized_long_3pc)

mhlist_ref_short = array('d',mhlist_ref_short)
mhlist_optimized_long = array('d',mhlist_optimized_long)
mhlist_ref_short_3pc = array('d',mhlist_ref_short_3pc)
mhlist_optimized_long_3pc = array('d',mhlist_optimized_long_3pc)

mhlistbest_ref_short = array('d',mhlistbest_ref_short)
mhlistbest_optimized_long = array('d',mhlistbest_optimized_long)
mhlistbest_ref_short_3pc = array('d',mhlistbest_ref_short_3pc)
mhlistbest_optimized_long_3pc = array('d',mhlistbest_optimized_long_3pc)

g_cpvsig_75_ref_short = ROOT.TGraph(n,explist,cpvlist75_ref_short)
g_cpvsig_75_optimized_long = ROOT.TGraph(n,explist,cpvlist75_optimized_long)
g_cpvsig_75_ref_short_3pc = ROOT.TGraph(n,explist,cpvlist75_ref_short_3pc)
g_cpvsig_75_optimized_long_3pc = ROOT.TGraph(n,explist,cpvlist75_optimized_long_3pc)

g_cpvsig_50_ref_short = ROOT.TGraph(n,explist,cpvlist50_ref_short)
g_cpvsig_50_optimized_long = ROOT.TGraph(n,explist,cpvlist50_optimized_long)
g_cpvsig_50_ref_short_3pc = ROOT.TGraph(n,explist,cpvlist50_ref_short_3pc)
g_cpvsig_50_optimized_long_3pc = ROOT.TGraph(n,explist,cpvlist50_optimized_long_3pc)

g_cpvsigbest_ref_short = ROOT.TGraph(n,explist,cpvlistbest_ref_short)
g_cpvsigbest_optimized_long = ROOT.TGraph(n,explist,cpvlistbest_optimized_long)
g_cpvsigbest_ref_short_3pc = ROOT.TGraph(n,explist,cpvlistbest_ref_short_3pc)
g_cpvsigbest_optimized_long_3pc = ROOT.TGraph(n,explist,cpvlistbest_optimized_long_3pc)

g_mhsig_100_ref_short = ROOT.TGraph(n,explist,mhlist_ref_short)
g_mhsig_100_optimized_long = ROOT.TGraph(n,explist,mhlist_optimized_long)
g_mhsig_100_ref_short_3pc = ROOT.TGraph(n,explist,mhlist_ref_short_3pc)
g_mhsig_100_optimized_long_3pc = ROOT.TGraph(n,explist,mhlist_optimized_long_3pc)

g_mhsigbest_ref_short = ROOT.TGraph(n,explist,mhlistbest_ref_short)
g_mhsigbest_optimized_long = ROOT.TGraph(n,explist,mhlistbest_optimized_long)
g_mhsigbest_ref_short_3pc = ROOT.TGraph(n,explist,mhlistbest_ref_short_3pc)
g_mhsigbest_optimized_long_3pc = ROOT.TGraph(n,explist,mhlistbest_optimized_long_3pc)

g_cpvsig_75_ref_short.SetLineWidth(3)
g_cpvsig_75_ref_short_3pc.SetLineWidth(3)
g_cpvsig_75_optimized_long.SetLineWidth(3)
g_cpvsig_75_optimized_long_3pc.SetLineWidth(3)
g_cpvsig_75_ref_short.SetLineColor(ROOT.kBlue-1)
g_cpvsig_75_ref_short_3pc.SetLineColor(ROOT.kBlue-1)
g_cpvsig_75_optimized_long.SetLineColor(ROOT.kGreen-1)
g_cpvsig_75_optimized_long_3pc.SetLineColor(ROOT.kGreen-1)

g_cpvsig_50_ref_short.SetLineWidth(3)
g_cpvsig_50_ref_short_3pc.SetLineWidth(3)
g_cpvsig_50_optimized_long.SetLineWidth(3)
g_cpvsig_50_optimized_long_3pc.SetLineWidth(3)
g_cpvsig_50_ref_short.SetLineColor(ROOT.kBlue-1)
g_cpvsig_50_ref_short_3pc.SetLineColor(ROOT.kBlue-1)
g_cpvsig_50_optimized_long.SetLineColor(ROOT.kGreen-1)
g_cpvsig_50_optimized_long_3pc.SetLineColor(ROOT.kGreen-1)

g_cpvsigbest_ref_short.SetLineWidth(3)
g_cpvsigbest_ref_short_3pc.SetLineWidth(3)
g_cpvsigbest_optimized_long.SetLineWidth(3)
g_cpvsigbest_optimized_long_3pc.SetLineWidth(3)
g_cpvsigbest_ref_short.SetLineColor(ROOT.kBlue-1)
g_cpvsigbest_ref_short_3pc.SetLineColor(ROOT.kBlue-1)
g_cpvsigbest_optimized_long.SetLineColor(ROOT.kGreen-1)
g_cpvsigbest_optimized_long_3pc.SetLineColor(ROOT.kGreen-1)

g_mhsig_100_ref_short.SetLineWidth(3)
g_mhsig_100_ref_short_3pc.SetLineWidth(3)
g_mhsig_100_optimized_long.SetLineWidth(3)
g_mhsig_100_optimized_long_3pc.SetLineWidth(3)
g_mhsig_100_ref_short.SetLineColor(ROOT.kBlue-1)
g_mhsig_100_ref_short_3pc.SetLineColor(ROOT.kBlue-1)
g_mhsig_100_optimized_long.SetLineColor(ROOT.kGreen-1)
g_mhsig_100_optimized_long_3pc.SetLineColor(ROOT.kGreen-1)

g_mhsigbest_ref_short.SetLineWidth(3)
g_mhsigbest_ref_short_3pc.SetLineWidth(3)
g_mhsigbest_optimized_long.SetLineWidth(3)
g_mhsigbest_optimized_long_3pc.SetLineWidth(3)
g_mhsigbest_ref_short.SetLineColor(ROOT.kBlue-1)
g_mhsigbest_ref_short_3pc.SetLineColor(ROOT.kBlue-1)
g_mhsigbest_optimized_long.SetLineColor(ROOT.kGreen-1)
g_mhsigbest_optimized_long_3pc.SetLineColor(ROOT.kGreen-1)

#Get resolutions
r1 = ROOT.TFile("root/resdcp0_optimized_long_no_noconstr.root")
g_res_ref = r1.Get("Res")
r2 = ROOT.TFile("root/resdcp0_optimized_long_syst3pc_no_noconstr.root")
g_res_ref_3pc = r2.Get("Res")
r4 = ROOT.TFile("root/resdcp0_optimized_long_no.root")
g_res_opt = r4.Get("Res")
r5 = ROOT.TFile("root/resdcp0_optimized_long_syst3pc_no.root")
g_res_opt_3pc = r5.Get("Res")

r190 = ROOT.TFile("root/resdcp-90_optimized_long_no_noconstr.root")
g_res_ref90 = r190.Get("Res")
r290 = ROOT.TFile("root/resdcp-90_optimized_long_syst3pc_no_noconstr.root")
g_res_ref90_3pc = r290.Get("Res")
r490 = ROOT.TFile("root/resdcp-90_optimized_long_no.root")
g_res_opt90 = r490.Get("Res")
r590 = ROOT.TFile("root/resdcp-90_optimized_long_syst3pc_no.root")
g_res_opt90_3pc = r590.Get("Res")

years = [0,0.25,0.5,0.75,1,1.25,1.5,2,2.5,3,3.5,4,4.5,5,6,7,8,9,10,11,12,13,14,15]
cpv75_ref = [0]
cpv50_ref = [0]
cpvbest_ref = [0]
mh_ref = [0]
mhbest_ref = [0]
res_ref = [999]
res_ref90 = [999]
cpv75_opt = [0]
cpv50_opt = [0]
cpvbest_opt = [0]
mh_opt = [0]
mhbest_opt = [0]
res_opt = [999]
res_opt90 = [999]

#Year 0.25: 20kt * 1.07 MW, 3% syst = 5.35 kt-MW-yr
thisexp = 5.35
print "Year 0.25: ", thisexp
cpv75_ref.append(g_cpvsig_75_ref_short_3pc.Eval(thisexp,0,"S"))
cpv50_ref.append(g_cpvsig_50_ref_short_3pc.Eval(thisexp,0,"S"))
cpvbest_ref.append(g_cpvsigbest_ref_short_3pc.Eval(thisexp,0,"S"))
mh_ref.append(g_mhsig_100_ref_short_3pc.Eval(thisexp,0,"S"))
mhbest_ref.append(g_mhsigbest_ref_short_3pc.Eval(thisexp,0,"S"))
res_ref.append(g_res_ref_3pc.Eval(thisexp,0,""))
res_ref90.append(g_res_ref90_3pc.Eval(thisexp,0,""))
cpv75_opt.append(g_cpvsig_75_optimized_long_3pc.Eval(thisexp,0,"S"))
cpv50_opt.append(g_cpvsig_50_optimized_long_3pc.Eval(thisexp,0,"S"))
cpvbest_opt.append(g_cpvsigbest_optimized_long_3pc.Eval(thisexp,0,"S"))
mh_opt.append(g_mhsig_100_optimized_long_3pc.Eval(thisexp,0,"S"))
mhbest_opt.append(g_mhsigbest_optimized_long_3pc.Eval(thisexp,0,"S"))
res_opt.append(g_res_opt_3pc.Eval(thisexp,0,""))
res_opt90.append(g_res_opt90_3pc.Eval(thisexp,0,""))

#Year 0.5: 20kt * 1.07 MW, 3% syst = 10.7 kt-MW-yr
thisexp = 10.7
print "Year 0.5: ", thisexp
cpv75_ref.append(g_cpvsig_75_ref_short_3pc.Eval(thisexp,0,"S"))
cpv50_ref.append(g_cpvsig_50_ref_short_3pc.Eval(thisexp,0,"S"))
cpvbest_ref.append(g_cpvsigbest_ref_short_3pc.Eval(thisexp,0,"S"))
mh_ref.append(g_mhsig_100_ref_short_3pc.Eval(thisexp,0,"S"))
mhbest_ref.append(g_mhsigbest_ref_short_3pc.Eval(thisexp,0,"S"))
res_ref.append(g_res_ref_3pc.Eval(thisexp,0,""))
res_ref90.append(g_res_ref90_3pc.Eval(thisexp,0,""))
cpv75_opt.append(g_cpvsig_75_optimized_long_3pc.Eval(thisexp,0,"S"))
cpv50_opt.append(g_cpvsig_50_optimized_long_3pc.Eval(thisexp,0,"S"))
cpvbest_opt.append(g_cpvsigbest_optimized_long_3pc.Eval(thisexp,0,"S"))
mh_opt.append(g_mhsig_100_optimized_long_3pc.Eval(thisexp,0,"S"))
mhbest_opt.append(g_mhsigbest_optimized_long_3pc.Eval(thisexp,0,"S"))
res_opt.append(g_res_opt_3pc.Eval(thisexp,0,""))
res_opt90.append(g_res_opt90_3pc.Eval(thisexp,0,""))

#Year 0.75: 20kt * 1.07 MW, 3% syst = 16.05 kt-MW-yr
thisexp = 16.05
print "Year 0.75: ", thisexp
cpv75_ref.append(g_cpvsig_75_ref_short_3pc.Eval(thisexp,0,"S"))
cpv50_ref.append(g_cpvsig_50_ref_short_3pc.Eval(thisexp,0,"S"))
cpvbest_ref.append(g_cpvsigbest_ref_short_3pc.Eval(thisexp,0,"S"))
mh_ref.append(g_mhsig_100_ref_short_3pc.Eval(thisexp,0,"S"))
mhbest_ref.append(g_mhsigbest_ref_short_3pc.Eval(thisexp,0,"S"))
res_ref.append(g_res_ref_3pc.Eval(thisexp,0,""))
res_ref90.append(g_res_ref90_3pc.Eval(thisexp,0,""))
cpv75_opt.append(g_cpvsig_75_optimized_long_3pc.Eval(thisexp,0,"S"))
cpv50_opt.append(g_cpvsig_50_optimized_long_3pc.Eval(thisexp,0,"S"))
cpvbest_opt.append(g_cpvsigbest_optimized_long_3pc.Eval(thisexp,0,"S"))
mh_opt.append(g_mhsig_100_optimized_long_3pc.Eval(thisexp,0,"S"))
mhbest_opt.append(g_mhsigbest_optimized_long_3pc.Eval(thisexp,0,"S"))
res_opt.append(g_res_opt_3pc.Eval(thisexp,0,""))
res_opt90.append(g_res_opt90_3pc.Eval(thisexp,0,""))


#Year 1: 20kt * 1.07 MW, 3% syst = 21.4 kt-MW-yr
thisexp = 21.4
print "Year 1: ", thisexp
cpv75_ref.append(g_cpvsig_75_ref_short_3pc.Eval(thisexp,0,"S"))
cpv50_ref.append(g_cpvsig_50_ref_short_3pc.Eval(thisexp,0,"S"))
cpvbest_ref.append(g_cpvsigbest_ref_short_3pc.Eval(thisexp,0,"S"))
mh_ref.append(g_mhsig_100_ref_short_3pc.Eval(thisexp,0,"S"))
mhbest_ref.append(g_mhsigbest_ref_short_3pc.Eval(thisexp,0,"S"))
res_ref.append(g_res_ref_3pc.Eval(thisexp,0,""))
res_ref90.append(g_res_ref90_3pc.Eval(thisexp,0,""))
cpv75_opt.append(g_cpvsig_75_optimized_long_3pc.Eval(thisexp,0,"S"))
cpv50_opt.append(g_cpvsig_50_optimized_long_3pc.Eval(thisexp,0,"S"))
cpvbest_opt.append(g_cpvsigbest_optimized_long_3pc.Eval(thisexp,0,"S"))
mh_opt.append(g_mhsig_100_optimized_long_3pc.Eval(thisexp,0,"S"))
mhbest_opt.append(g_mhsigbest_optimized_long_3pc.Eval(thisexp,0,"S"))
res_opt.append(g_res_opt_3pc.Eval(thisexp,0,""))
res_opt90.append(g_res_opt90_3pc.Eval(thisexp,0,""))

#Year 1.25: + 30kt * 1.07 MW, 3% syst = 53.5 kt-MW-yr
thisexp += 30*1.07*0.25
print "Year 1.5: ", thisexp
cpv75_ref.append(g_cpvsig_75_ref_short_3pc.Eval(thisexp,0,"S"))
cpv50_ref.append(g_cpvsig_50_ref_short_3pc.Eval(thisexp,0,"S"))
cpvbest_ref.append(g_cpvsigbest_ref_short_3pc.Eval(thisexp,0,"S"))
mh_ref.append(g_mhsig_100_ref_short_3pc.Eval(thisexp,0,"S"))
mhbest_ref.append(g_mhsigbest_ref_short_3pc.Eval(thisexp,0,"S"))
res_ref.append(g_res_ref_3pc.Eval(thisexp,0,""))
res_ref90.append(g_res_ref90_3pc.Eval(thisexp,0,""))
cpv75_opt.append(g_cpvsig_75_optimized_long_3pc.Eval(thisexp,0,"S"))
cpv50_opt.append(g_cpvsig_50_optimized_long_3pc.Eval(thisexp,0,"S"))
cpvbest_opt.append(g_cpvsigbest_optimized_long_3pc.Eval(thisexp,0,"S"))
mh_opt.append(g_mhsig_100_optimized_long_3pc.Eval(thisexp,0,"S"))
mhbest_opt.append(g_mhsigbest_optimized_long_3pc.Eval(thisexp,0,"S"))
res_opt.append(g_res_opt_3pc.Eval(thisexp,0,""))
res_opt90.append(g_res_opt90_3pc.Eval(thisexp,0,""))

#Year 1.5: + 30kt * 1.07 MW, 3% syst = 53.5 kt-MW-yr
thisexp += 30*1.07*0.25
print "Year 1.5: ", thisexp
cpv75_ref.append(g_cpvsig_75_ref_short_3pc.Eval(thisexp,0,"S"))
cpv50_ref.append(g_cpvsig_50_ref_short_3pc.Eval(thisexp,0,"S"))
cpvbest_ref.append(g_cpvsigbest_ref_short_3pc.Eval(thisexp,0,"S"))
mh_ref.append(g_mhsig_100_ref_short_3pc.Eval(thisexp,0,"S"))
mhbest_ref.append(g_mhsigbest_ref_short_3pc.Eval(thisexp,0,"S"))
res_ref.append(g_res_ref_3pc.Eval(thisexp,0,""))
res_ref90.append(g_res_ref90_3pc.Eval(thisexp,0,""))
cpv75_opt.append(g_cpvsig_75_optimized_long_3pc.Eval(thisexp,0,"S"))
cpv50_opt.append(g_cpvsig_50_optimized_long_3pc.Eval(thisexp,0,"S"))
cpvbest_opt.append(g_cpvsigbest_optimized_long_3pc.Eval(thisexp,0,"S"))
mh_opt.append(g_mhsig_100_optimized_long_3pc.Eval(thisexp,0,"S"))
mhbest_opt.append(g_mhsigbest_optimized_long_3pc.Eval(thisexp,0,"S"))
res_opt.append(g_res_opt_3pc.Eval(thisexp,0,""))
res_opt90.append(g_res_opt90_3pc.Eval(thisexp,0,""))

#Year 2: + 30kt * 1.07 MW, 3% syst = 53.5 kt-MW-yr
thisexp += 30*1.07*0.5
print "Year 2: ", thisexp
cpv75_ref.append(g_cpvsig_75_ref_short_3pc.Eval(thisexp,0,"S"))
cpv50_ref.append(g_cpvsig_50_ref_short_3pc.Eval(thisexp,0,"S"))
cpvbest_ref.append(g_cpvsigbest_ref_short_3pc.Eval(thisexp,0,"S"))
mh_ref.append(g_mhsig_100_ref_short_3pc.Eval(thisexp,0,"S"))
mhbest_ref.append(g_mhsigbest_ref_short_3pc.Eval(thisexp,0,"S"))
res_ref.append(g_res_ref_3pc.Eval(thisexp,0,""))
res_ref90.append(g_res_ref90_3pc.Eval(thisexp,0,""))
cpv75_opt.append(g_cpvsig_75_optimized_long_3pc.Eval(thisexp,0,"S"))
cpv50_opt.append(g_cpvsig_50_optimized_long_3pc.Eval(thisexp,0,"S"))
cpvbest_opt.append(g_cpvsigbest_optimized_long_3pc.Eval(thisexp,0,"S"))
mh_opt.append(g_mhsig_100_optimized_long_3pc.Eval(thisexp,0,"S"))
mhbest_opt.append(g_mhsigbest_optimized_long_3pc.Eval(thisexp,0,"S"))
res_opt.append(g_res_opt_3pc.Eval(thisexp,0,""))
res_opt90.append(g_res_opt90_3pc.Eval(thisexp,0,""))

#Year 2.5: + 30kt * 1.07 MW, 3% syst = 53.5 kt-MW-yr
thisexp += 30*1.07*0.5
print "Year 2.5: ", thisexp
cpv75_ref.append(g_cpvsig_75_ref_short_3pc.Eval(thisexp,0,"S"))
cpv50_ref.append(g_cpvsig_50_ref_short_3pc.Eval(thisexp,0,"S"))
cpvbest_ref.append(g_cpvsigbest_ref_short_3pc.Eval(thisexp,0,"S"))
mh_ref.append(g_mhsig_100_ref_short_3pc.Eval(thisexp,0,"S"))
mhbest_ref.append(g_mhsigbest_ref_short_3pc.Eval(thisexp,0,"S"))
res_ref.append(g_res_ref_3pc.Eval(thisexp,0,""))
res_ref90.append(g_res_ref90_3pc.Eval(thisexp,0,""))
cpv75_opt.append(g_cpvsig_75_optimized_long_3pc.Eval(thisexp,0,"S"))
cpv50_opt.append(g_cpvsig_50_optimized_long_3pc.Eval(thisexp,0,"S"))
cpvbest_opt.append(g_cpvsigbest_optimized_long_3pc.Eval(thisexp,0,"S"))
mh_opt.append(g_mhsig_100_optimized_long_3pc.Eval(thisexp,0,"S"))
mhbest_opt.append(g_mhsigbest_optimized_long_3pc.Eval(thisexp,0,"S"))
res_opt.append(g_res_opt_3pc.Eval(thisexp,0,""))
res_opt90.append(g_res_opt90_3pc.Eval(thisexp,0,""))

#Year 3: + 30kt * 1.07 MW, 3% syst = 85.6 kt-MW-yr
thisexp += 30*1.07*0.5
print "Year 3: ", thisexp
cpv75_ref.append(g_cpvsig_75_ref_short_3pc.Eval(thisexp,0,"S"))
cpv50_ref.append(g_cpvsig_50_ref_short_3pc.Eval(thisexp,0,"S"))
cpvbest_ref.append(g_cpvsigbest_ref_short_3pc.Eval(thisexp,0,"S"))
mh_ref.append(g_mhsig_100_ref_short_3pc.Eval(thisexp,0,"S"))
mhbest_ref.append(g_mhsigbest_ref_short_3pc.Eval(thisexp,0,"S"))
res_ref.append(g_res_ref_3pc.Eval(thisexp,0,""))
res_ref90.append(g_res_ref90_3pc.Eval(thisexp,0,""))
cpv75_opt.append(g_cpvsig_75_optimized_long_3pc.Eval(thisexp,0,"S"))
cpv50_opt.append(g_cpvsig_50_optimized_long_3pc.Eval(thisexp,0,"S"))
cpvbest_opt.append(g_cpvsigbest_optimized_long_3pc.Eval(thisexp,0,"S"))
mh_opt.append(g_mhsig_100_optimized_long_3pc.Eval(thisexp,0,"S"))
mhbest_opt.append(g_mhsigbest_optimized_long_3pc.Eval(thisexp,0,"S"))
res_opt.append(g_res_opt_3pc.Eval(thisexp,0,""))
res_opt90.append(g_res_opt90_3pc.Eval(thisexp,0,""))

#Year 3.5: + 40kt * 1.07 MW, 2% syst 
thisexp += 40*1.07*0.5
print "Year 3.5: ", thisexp
cpv75_ref.append(g_cpvsig_75_ref_short.Eval(thisexp,0,"S"))
cpv50_ref.append(g_cpvsig_50_ref_short.Eval(thisexp,0,"S"))
cpvbest_ref.append(g_cpvsigbest_ref_short.Eval(thisexp,0,"S"))
mh_ref.append(g_mhsig_100_ref_short.Eval(thisexp,0,"S"))
mhbest_ref.append(g_mhsigbest_ref_short.Eval(thisexp,0,"S"))
res_ref.append(g_res_ref.Eval(thisexp,0,""))
res_ref90.append(g_res_ref90.Eval(thisexp,0,""))
cpv75_opt.append(g_cpvsig_75_optimized_long.Eval(thisexp,0,"S"))
cpv50_opt.append(g_cpvsig_50_optimized_long.Eval(thisexp,0,"S"))
cpvbest_opt.append(g_cpvsigbest_optimized_long.Eval(thisexp,0,"S"))
mh_opt.append(g_mhsig_100_optimized_long.Eval(thisexp,0,"S"))
mhbest_opt.append(g_mhsigbest_optimized_long.Eval(thisexp,0,"S"))
res_opt.append(g_res_opt.Eval(thisexp,0,""))
res_opt90.append(g_res_opt90.Eval(thisexp,0,""))

#Year 4: + 40kt * 1.07 MW, 2% syst = 128.4 kt-MW-yr
thisexp += 40*1.07*0.5
print "Year 4: ", thisexp
cpv75_ref.append(g_cpvsig_75_ref_short.Eval(thisexp,0,"S"))
cpv50_ref.append(g_cpvsig_50_ref_short.Eval(thisexp,0,"S"))
cpvbest_ref.append(g_cpvsigbest_ref_short.Eval(thisexp,0,"S"))
mh_ref.append(g_mhsig_100_ref_short.Eval(thisexp,0,"S"))
mhbest_ref.append(g_mhsigbest_ref_short.Eval(thisexp,0,"S"))
res_ref.append(g_res_ref.Eval(thisexp,0,""))
res_ref90.append(g_res_ref90.Eval(thisexp,0,""))
cpv75_opt.append(g_cpvsig_75_optimized_long.Eval(thisexp,0,"S"))
cpv50_opt.append(g_cpvsig_50_optimized_long.Eval(thisexp,0,"S"))
cpvbest_opt.append(g_cpvsigbest_optimized_long.Eval(thisexp,0,"S"))
mh_opt.append(g_mhsig_100_optimized_long.Eval(thisexp,0,"S"))
mhbest_opt.append(g_mhsigbest_optimized_long.Eval(thisexp,0,"S"))
res_opt.append(g_res_opt.Eval(thisexp,0,""))
res_opt90.append(g_res_opt90.Eval(thisexp,0,""))

#Year 4.5: + 40kt * 1.07 MW, 2% syst 
thisexp += 40*1.07*0.5
print "Year 4.5: ", thisexp
cpv75_ref.append(g_cpvsig_75_ref_short.Eval(thisexp,0,"S"))
cpv50_ref.append(g_cpvsig_50_ref_short.Eval(thisexp,0,"S"))
cpvbest_ref.append(g_cpvsigbest_ref_short.Eval(thisexp,0,"S"))
mh_ref.append(g_mhsig_100_ref_short.Eval(thisexp,0,"S"))
mhbest_ref.append(g_mhsigbest_ref_short.Eval(thisexp,0,"S"))
res_ref.append(g_res_ref.Eval(thisexp,0,""))
res_ref90.append(g_res_ref90.Eval(thisexp,0,""))
cpv75_opt.append(g_cpvsig_75_optimized_long.Eval(thisexp,0,"S"))
cpv50_opt.append(g_cpvsig_50_optimized_long.Eval(thisexp,0,"S"))
cpvbest_opt.append(g_cpvsigbest_optimized_long.Eval(thisexp,0,"S"))
mh_opt.append(g_mhsig_100_optimized_long.Eval(thisexp,0,"S"))
mhbest_opt.append(g_mhsigbest_optimized_long.Eval(thisexp,0,"S"))
res_opt.append(g_res_opt.Eval(thisexp,0,""))
res_opt90.append(g_res_opt90.Eval(thisexp,0,""))

#Year 5: + 40kt * 1.07 MW, 2% syst = 171.2 kt-MW-yr
thisexp += 40*1.07*0.5
print "Year 5: ", thisexp
cpv75_ref.append(g_cpvsig_75_ref_short.Eval(thisexp,0,"S"))
cpv50_ref.append(g_cpvsig_50_ref_short.Eval(thisexp,0,"S"))
cpvbest_ref.append(g_cpvsigbest_ref_short.Eval(thisexp,0,"S"))
mh_ref.append(g_mhsig_100_ref_short.Eval(thisexp,0,"S"))
mhbest_ref.append(g_mhsigbest_ref_short.Eval(thisexp,0,"S"))
res_ref.append(g_res_ref.Eval(thisexp,0,""))
res_ref90.append(g_res_ref90.Eval(thisexp,0,""))
cpv75_opt.append(g_cpvsig_75_optimized_long.Eval(thisexp,0,"S"))
cpv50_opt.append(g_cpvsig_50_optimized_long.Eval(thisexp,0,"S"))
cpvbest_opt.append(g_cpvsigbest_optimized_long.Eval(thisexp,0,"S"))
mh_opt.append(g_mhsig_100_optimized_long.Eval(thisexp,0,"S"))
mhbest_opt.append(g_mhsigbest_optimized_long.Eval(thisexp,0,"S"))
res_opt.append(g_res_opt.Eval(thisexp,0,""))
res_opt90.append(g_res_opt90.Eval(thisexp,0,""))

#Year 6: + 40kt * 1.07 MW, 2% syst = 214 kt-MW-yr
thisexp += 40*1.07
print "Year 6: ", thisexp
cpv75_ref.append(g_cpvsig_75_ref_short.Eval(thisexp,0,"S"))
cpv50_ref.append(g_cpvsig_50_ref_short.Eval(thisexp,0,"S"))
cpvbest_ref.append(g_cpvsigbest_ref_short.Eval(thisexp,0,"S"))
mh_ref.append(g_mhsig_100_ref_short.Eval(thisexp,0,"S"))
mhbest_ref.append(g_mhsigbest_ref_short.Eval(thisexp,0,"S"))
res_ref.append(g_res_ref.Eval(thisexp,0,""))
res_ref90.append(g_res_ref90.Eval(thisexp,0,""))
cpv75_opt.append(g_cpvsig_75_optimized_long.Eval(thisexp,0,"S"))
cpv50_opt.append(g_cpvsig_50_optimized_long.Eval(thisexp,0,"S"))
cpvbest_opt.append(g_cpvsigbest_optimized_long.Eval(thisexp,0,"S"))
mh_opt.append(g_mhsig_100_optimized_long.Eval(thisexp,0,"S"))
mhbest_opt.append(g_mhsigbest_optimized_long.Eval(thisexp,0,"S"))
res_opt.append(g_res_opt.Eval(thisexp,0,""))
res_opt90.append(g_res_opt90.Eval(thisexp,0,""))

#Year 7: + 40kt * 2.14 MW, 2% syst = 299.6 kt-MW-yr
thisexp += 40*2.14
print "Year 7: ", thisexp
cpv75_ref.append(g_cpvsig_75_ref_short.Eval(thisexp,0,"S"))
cpv50_ref.append(g_cpvsig_50_ref_short.Eval(thisexp,0,"S"))
cpvbest_ref.append(g_cpvsigbest_ref_short.Eval(thisexp,0,"S"))
mh_ref.append(g_mhsig_100_ref_short.Eval(thisexp,0,"S"))
mhbest_ref.append(g_mhsigbest_ref_short.Eval(thisexp,0,"S"))
res_ref.append(g_res_ref.Eval(thisexp,0,"S"))
res_ref90.append(g_res_ref90.Eval(thisexp,0,"S"))
cpv75_opt.append(g_cpvsig_75_optimized_long.Eval(thisexp,0,"S"))
cpv50_opt.append(g_cpvsig_50_optimized_long.Eval(thisexp,0,"S"))
cpvbest_opt.append(g_cpvsigbest_optimized_long.Eval(thisexp,0,"S"))
mh_opt.append(g_mhsig_100_optimized_long.Eval(thisexp,0,"S"))
mhbest_opt.append(g_mhsigbest_optimized_long.Eval(thisexp,0,"S"))
res_opt.append(g_res_opt.Eval(thisexp,0,"S"))
res_opt90.append(g_res_opt90.Eval(thisexp,0,"S"))

#Year 8: + 40kt * 2.14 MW, 2% syst
thisexp += 40*2.14
print "Year 8: ", thisexp
cpv75_ref.append(g_cpvsig_75_ref_short.Eval(thisexp,0,"S"))
cpv50_ref.append(g_cpvsig_50_ref_short.Eval(thisexp,0,"S"))
cpvbest_ref.append(g_cpvsigbest_ref_short.Eval(thisexp,0,"S"))
mh_ref.append(g_mhsig_100_ref_short.Eval(thisexp,0,"S"))
mhbest_ref.append(g_mhsigbest_ref_short.Eval(thisexp,0,"S"))
res_ref.append(g_res_ref.Eval(thisexp,0,"S"))
res_ref90.append(g_res_ref90.Eval(thisexp,0,"S"))
cpv75_opt.append(g_cpvsig_75_optimized_long.Eval(thisexp,0,"S"))
cpv50_opt.append(g_cpvsig_50_optimized_long.Eval(thisexp,0,"S"))
cpvbest_opt.append(g_cpvsigbest_optimized_long.Eval(thisexp,0,"S"))
mh_opt.append(g_mhsig_100_optimized_long.Eval(thisexp,0,"S"))
mhbest_opt.append(g_mhsigbest_optimized_long.Eval(thisexp,0,"S"))
res_opt.append(g_res_opt.Eval(thisexp,0,"S"))
res_opt90.append(g_res_opt90.Eval(thisexp,0,"S"))

#Year 9: + 40kt * 2.14 MW, 2% syst
thisexp += 40*2.14
print "Year 9: ", thisexp
cpv75_ref.append(g_cpvsig_75_ref_short.Eval(thisexp,0,"S"))
cpv50_ref.append(g_cpvsig_50_ref_short.Eval(thisexp,0,"S"))
cpvbest_ref.append(g_cpvsigbest_ref_short.Eval(thisexp,0,"S"))
mh_ref.append(g_mhsig_100_ref_short.Eval(thisexp,0,"S"))
mhbest_ref.append(g_mhsigbest_ref_short.Eval(thisexp,0,"S"))
res_ref.append(g_res_ref.Eval(thisexp,0,"S"))
res_ref90.append(g_res_ref90.Eval(thisexp,0,"S"))
cpv75_opt.append(g_cpvsig_75_optimized_long.Eval(thisexp,0,"S"))
cpv50_opt.append(g_cpvsig_50_optimized_long.Eval(thisexp,0,"S"))
cpvbest_opt.append(g_cpvsigbest_optimized_long.Eval(thisexp,0,"S"))
mh_opt.append(g_mhsig_100_optimized_long.Eval(thisexp,0,"S"))
mhbest_opt.append(g_mhsigbest_optimized_long.Eval(thisexp,0,"S"))
res_opt.append(g_res_opt.Eval(thisexp,0,"S"))
res_opt90.append(g_res_opt90.Eval(thisexp,0,"S"))

#Year 10: + 40kt * 2.14 MW, 2% syst
thisexp += 40*2.14
print "Year 10: ", thisexp
cpv75_ref.append(g_cpvsig_75_ref_short.Eval(thisexp,0,"S"))
cpv50_ref.append(g_cpvsig_50_ref_short.Eval(thisexp,0,"S"))
cpvbest_ref.append(g_cpvsigbest_ref_short.Eval(thisexp,0,"S"))
mh_ref.append(g_mhsig_100_ref_short.Eval(thisexp,0,"S"))
mhbest_ref.append(g_mhsigbest_ref_short.Eval(thisexp,0,"S"))
res_ref.append(g_res_ref.Eval(thisexp,0,"S"))
res_ref90.append(g_res_ref90.Eval(thisexp,0,"S"))
cpv75_opt.append(g_cpvsig_75_optimized_long.Eval(thisexp,0,"S"))
cpv50_opt.append(g_cpvsig_50_optimized_long.Eval(thisexp,0,"S"))
cpvbest_opt.append(g_cpvsigbest_optimized_long.Eval(thisexp,0,"S"))
mh_opt.append(g_mhsig_100_optimized_long.Eval(thisexp,0,"S"))
mhbest_opt.append(g_mhsigbest_optimized_long.Eval(thisexp,0,"S"))
res_opt.append(g_res_opt.Eval(thisexp,0,"S"))
res_opt90.append(g_res_opt90.Eval(thisexp,0,"S"))

#Year 11: + 40kt * 2.14 MW, 2% syst
thisexp += 40*2.14
print "Year 11: ", thisexp
cpv75_ref.append(g_cpvsig_75_ref_short.Eval(thisexp,0,"S"))
cpv50_ref.append(g_cpvsig_50_ref_short.Eval(thisexp,0,"S"))
cpvbest_ref.append(g_cpvsigbest_ref_short.Eval(thisexp,0,"S"))
mh_ref.append(g_mhsig_100_ref_short.Eval(thisexp,0,"S"))
mhbest_ref.append(g_mhsigbest_ref_short.Eval(thisexp,0,"S"))
res_ref.append(g_res_ref.Eval(thisexp,0,"S"))
res_ref90.append(g_res_ref90.Eval(thisexp,0,"S"))
cpv75_opt.append(g_cpvsig_75_optimized_long.Eval(thisexp,0,"S"))
cpv50_opt.append(g_cpvsig_50_optimized_long.Eval(thisexp,0,"S"))
cpvbest_opt.append(g_cpvsigbest_optimized_long.Eval(thisexp,0,"S"))
mh_opt.append(g_mhsig_100_optimized_long.Eval(thisexp,0,"S"))
mhbest_opt.append(g_mhsigbest_optimized_long.Eval(thisexp,0,"S"))
res_opt.append(g_res_opt.Eval(thisexp,0,"S"))
res_opt90.append(g_res_opt90.Eval(thisexp,0,"S"))

#Year 12: + 40kt * 2.14 MW, 2% syst
thisexp += 40*2.14
print "Year 12: ", thisexp
cpv75_ref.append(g_cpvsig_75_ref_short.Eval(thisexp,0,"S"))
cpv50_ref.append(g_cpvsig_50_ref_short.Eval(thisexp,0,"S"))
cpvbest_ref.append(g_cpvsigbest_ref_short.Eval(thisexp,0,"S"))
mh_ref.append(g_mhsig_100_ref_short.Eval(thisexp,0,"S"))
mhbest_ref.append(g_mhsigbest_ref_short.Eval(thisexp,0,"S"))
res_ref.append(g_res_ref.Eval(thisexp,0,"S"))
res_ref90.append(g_res_ref90.Eval(thisexp,0,"S"))
cpv75_opt.append(g_cpvsig_75_optimized_long.Eval(thisexp,0,"S"))
cpv50_opt.append(g_cpvsig_50_optimized_long.Eval(thisexp,0,"S"))
cpvbest_opt.append(g_cpvsigbest_optimized_long.Eval(thisexp,0,"S"))
mh_opt.append(g_mhsig_100_optimized_long.Eval(thisexp,0,"S"))
mhbest_opt.append(g_mhsigbest_optimized_long.Eval(thisexp,0,"S"))
res_opt.append(g_res_opt.Eval(thisexp,0,"S"))
res_opt90.append(g_res_opt90.Eval(thisexp,0,"S"))

#Year 13: + 40kt * 2.14 MW, 2% syst
thisexp += 40*2.14
print "Year 13: ", thisexp
cpv75_ref.append(g_cpvsig_75_ref_short.Eval(thisexp,0,"S"))
cpv50_ref.append(g_cpvsig_50_ref_short.Eval(thisexp,0,"S"))
cpvbest_ref.append(g_cpvsigbest_ref_short.Eval(thisexp,0,"S"))
mh_ref.append(g_mhsig_100_ref_short.Eval(thisexp,0,"S"))
mhbest_ref.append(g_mhsigbest_ref_short.Eval(thisexp,0,"S"))
res_ref.append(g_res_ref.Eval(thisexp,0,"S"))
res_ref90.append(g_res_ref90.Eval(thisexp,0,"S"))
cpv75_opt.append(g_cpvsig_75_optimized_long.Eval(thisexp,0,"S"))
cpv50_opt.append(g_cpvsig_50_optimized_long.Eval(thisexp,0,"S"))
cpvbest_opt.append(g_cpvsigbest_optimized_long.Eval(thisexp,0,"S"))
mh_opt.append(g_mhsig_100_optimized_long.Eval(thisexp,0,"S"))
mhbest_opt.append(g_mhsigbest_optimized_long.Eval(thisexp,0,"S"))
res_opt.append(g_res_opt.Eval(thisexp,0,"S"))
res_opt90.append(g_res_opt90.Eval(thisexp,0,"S"))

#Year 14: + 40kt * 2.14 MW, 2% syst
thisexp += 40*2.14
print "Year 14: ", thisexp
cpv75_ref.append(g_cpvsig_75_ref_short.Eval(thisexp,0,"S"))
cpv50_ref.append(g_cpvsig_50_ref_short.Eval(thisexp,0,"S"))
cpvbest_ref.append(g_cpvsigbest_ref_short.Eval(thisexp,0,"S"))
mh_ref.append(g_mhsig_100_ref_short.Eval(thisexp,0,"S"))
mhbest_ref.append(g_mhsigbest_ref_short.Eval(thisexp,0,"S"))
res_ref.append(g_res_ref.Eval(thisexp,0,"S"))
res_ref90.append(g_res_ref90.Eval(thisexp,0,"S"))
cpv75_opt.append(g_cpvsig_75_optimized_long.Eval(thisexp,0,"S"))
cpv50_opt.append(g_cpvsig_50_optimized_long.Eval(thisexp,0,"S"))
cpvbest_opt.append(g_cpvsigbest_optimized_long.Eval(thisexp,0,"S"))
mh_opt.append(g_mhsig_100_optimized_long.Eval(thisexp,0,"S"))
mhbest_opt.append(g_mhsigbest_optimized_long.Eval(thisexp,0,"S"))
res_opt.append(g_res_opt.Eval(thisexp,0,"S"))
res_opt90.append(g_res_opt90.Eval(thisexp,0,"S"))

#Year 15: + 40kt * 2.14 MW, 2% syst
thisexp += 40*2.14
print "Year 15: ", thisexp
cpv75_ref.append(g_cpvsig_75_ref_short.Eval(thisexp,0,"S"))
cpv50_ref.append(g_cpvsig_50_ref_short.Eval(thisexp,0,"S"))
cpvbest_ref.append(g_cpvsigbest_ref_short.Eval(thisexp,0,"S"))
mh_ref.append(g_mhsig_100_ref_short.Eval(thisexp,0,"S"))
mhbest_ref.append(g_mhsigbest_ref_short.Eval(thisexp,0,"S"))
res_ref.append(g_res_ref.Eval(thisexp,0,"S"))
res_ref90.append(g_res_ref90.Eval(thisexp,0,"S"))
cpv75_opt.append(g_cpvsig_75_optimized_long.Eval(thisexp,0,"S"))
cpv50_opt.append(g_cpvsig_50_optimized_long.Eval(thisexp,0,"S"))
cpvbest_opt.append(g_cpvsigbest_optimized_long.Eval(thisexp,0,"S"))
mh_opt.append(g_mhsig_100_optimized_long.Eval(thisexp,0,"S"))
mhbest_opt.append(g_mhsigbest_optimized_long.Eval(thisexp,0,"S"))
res_opt.append(g_res_opt.Eval(thisexp,0,"S"))
res_opt90.append(g_res_opt90.Eval(thisexp,0,"S"))

nyears = len(years)
years = array('d',years)
cpv75_ref = array('d',cpv75_ref)
cpv50_ref = array('d',cpv50_ref)
cpvbest_ref = array('d',cpvbest_ref)
mh_ref = array('d',mh_ref)
mhbest_ref = array('d',mhbest_ref)
res_ref = array('d',res_ref)
res_ref90 = array('d',res_ref90)
cpv75_opt = array('d',cpv75_opt)
cpv50_opt = array('d',cpv50_opt)
cpvbest_opt = array('d',cpvbest_opt)
mh_opt = array('d',mh_opt)
mhbest_opt = array('d',mhbest_opt)
res_opt = array('d',res_opt)
res_opt90 = array('d',res_opt90)

g_staged_cpv75_ref = ROOT.TGraph(nyears,years,cpv75_ref)
g_staged_cpv50_ref = ROOT.TGraph(nyears,years,cpv50_ref)
g_staged_cpvbest_ref = ROOT.TGraph(nyears,years,cpvbest_ref)
g_staged_mh_ref = ROOT.TGraph(nyears,years,mh_ref)
g_staged_mhbest_ref = ROOT.TGraph(nyears,years,mhbest_ref)
g_staged_res_ref = ROOT.TGraph(nyears,years,res_ref)
g_staged_res_ref90 = ROOT.TGraph(nyears,years,res_ref90)
g_staged_cpv75_opt = ROOT.TGraph(nyears,years,cpv75_opt)
g_staged_cpv50_opt = ROOT.TGraph(nyears,years,cpv50_opt)
g_staged_cpvbest_opt = ROOT.TGraph(nyears,years,cpvbest_opt)
g_staged_mh_opt = ROOT.TGraph(nyears,years,mh_opt)
g_staged_mhbest_opt = ROOT.TGraph(nyears,years,mhbest_opt)
g_staged_res_opt = ROOT.TGraph(nyears,years,res_opt)
g_staged_res_opt90 = ROOT.TGraph(nyears,years,res_opt90)

gdiff_staged_cpv75 = filldiff(g_staged_cpv75_opt,g_staged_cpv75_ref)
gdiff_staged_cpv50 = filldiff(g_staged_cpv50_opt,g_staged_cpv50_ref)
gdiff_staged_cpvbest = filldiff(g_staged_cpvbest_opt,g_staged_cpvbest_ref)
gdiff_staged_mh = filldiff(g_staged_mh_opt,g_staged_mh_ref)
gdiff_staged_mhbest = filldiff(g_staged_mhbest_opt,g_staged_mhbest_ref)
gdiff_staged_res = filldiff(g_staged_res_ref,g_staged_res_opt)
gdiff_staged_res90 = filldiff(g_staged_res_ref90,g_staged_res_opt90)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0,0.0,15.0,12.0)
h1.SetTitle("CP Violation Sensitivity")
h1.GetXaxis().SetTitle("Years")
h1.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h1.GetYaxis().SetTitleOffset(1.5)
h1.GetYaxis().CenterTitle()
c1.Modified()

gdiff_staged_cpv75.SetFillColor(ROOT.kCyan+2)
g_staged_cpv75_ref.SetLineWidth(3)
g_staged_cpv75_opt.SetLineWidth(3)
g_staged_cpv75_ref.SetLineStyle(2)

gdiff_staged_cpv75.Draw("F same")
g_staged_cpv75_ref.Draw("same")
g_staged_cpv75_opt.Draw("same")

gdiff_staged_cpv50.SetFillColor(ROOT.kCyan-7)
g_staged_cpv50_ref.SetLineWidth(3)
g_staged_cpv50_opt.SetLineWidth(3)
g_staged_cpv50_ref.SetLineStyle(2)

gdiff_staged_cpv50.Draw("F same")
g_staged_cpv50_ref.Draw("same")
g_staged_cpv50_opt.Draw("same")

gdiff_staged_cpvbest.SetFillColor(ROOT.kPink-3)
g_staged_cpvbest_ref.SetLineWidth(3)
g_staged_cpvbest_opt.SetLineWidth(3)
g_staged_cpvbest_ref.SetLineStyle(2)

gdiff_staged_cpvbest.Draw("F same")
g_staged_cpvbest_ref.Draw("same")
g_staged_cpvbest_opt.Draw("same")

t1 = ROOT.TPaveText(0.16,0.75,0.45,0.89,"NDC")
t1.AddText("DUNE Sensitivity (Staged)")
t1.AddText("Normal Ordering")
t1.AddText("sin^{2}2#theta_{13} = 0.085 #pm 0.003")
t1.AddText("sin^{2}#theta_{23} = 0.441 #pm 0.042")
t1.SetBorderSize(0)
t1.SetFillStyle(0)
#t1.SetFillColor(ROOT.kWhite)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.55,0.72,0.88,0.89)
l1.AddEntry(gdiff_staged_cpvbest, "#delta_{CP} = -#pi/2","F")
l1.AddEntry(gdiff_staged_cpv50, "50% of #delta_{CP} values","F")
l1.AddEntry(gdiff_staged_cpv75, "75% of #delta_{CP} values","F")
l1.AddEntry(g_staged_cpv75_opt,"Nominal Analysis","L")
l1.AddEntry(g_staged_cpv75_ref,"#theta_{13} & #theta_{23} unconstrained","L")
l1.SetBorderSize(0)
l1.Draw("same")

line1 = ROOT.TLine(0.,3.,15.0,3.)
line1.SetLineStyle(2)
line1.SetLineWidth(3)
line1.Draw("same")

line2 = ROOT.TLine(0.0,5.,15.,5.)
line2.SetLineStyle(2)
line2.SetLineWidth(3)
line2.Draw("same")

t3sig = ROOT.TPaveText(50.,3.1,100.,3.3)
t3sig.AddText("3#sigma")
t3sig.SetFillColor(0)
t3sig.SetBorderSize(0)
t3sig.Draw("same")

t5sig = ROOT.TPaveText(50.,5.1,100.,5.3)
t5sig.AddText("5#sigma")
t5sig.SetFillColor(0)
t5sig.SetBorderSize(0)
t5sig.Draw("same")

outname = "plots/cpv_exp_staging_varyconstr_2017.eps"
c1.SaveAs(outname)


c3 = ROOT.TCanvas("c3","c3",800,800)
c3.SetLeftMargin(0.15)
h3 = c3.DrawFrame(0,0.0,9.5,13.0)
#ROOT.gPad.SetTicks(0,1)
h3.SetTitle("MH Sensitivity")
h3.GetXaxis().SetTitle("Years")
h3.GetYaxis().SetTitle("#sqrt{#bar{#Delta#chi^{2}}}")
h3.GetYaxis().SetTitleOffset(1.3)
h3.GetYaxis().CenterTitle()
c3.Modified()

gdiff_staged_mh.SetFillColor(ROOT.kCyan+2)
g_staged_mh_ref.SetLineWidth(3)
g_staged_mh_opt.SetLineWidth(3)
g_staged_mh_ref.SetLineStyle(2)

gdiff_staged_mh.Draw("F same")
g_staged_mh_ref.Draw("same")
g_staged_mh_opt.Draw("same")

gdiff_staged_mhbest.SetFillColor(ROOT.kPink-3)
g_staged_mhbest_ref.SetLineWidth(3)
g_staged_mhbest_opt.SetLineWidth(3)
g_staged_mhbest_ref.SetLineStyle(2)

gdiff_staged_mhbest.Draw("F same")
g_staged_mhbest_ref.Draw("same")
g_staged_mhbest_opt.Draw("same")

t1.Draw("same")

lm1 = ROOT.TLegend(0.55,0.75,0.88,0.89)
lm1.AddEntry(gdiff_staged_mhbest, "#delta_{CP} = -#pi/2","F")
lm1.AddEntry(gdiff_staged_mh, "100% of #delta_{CP} values","F")
lm1.AddEntry(g_staged_mh_opt,"Nominal Analysis","L")
lm1.AddEntry(g_staged_mh_ref,"#theta_{13} & #theta_{23} unconstrained","L")
lm1.SetBorderSize(0)
lm1.Draw("same")

mhline1 = ROOT.TLine(0.,3.,9.5,3.)
mhline1.SetLineStyle(2)
mhline1.SetLineWidth(3)
mhline1.Draw("same")

mhline2 = ROOT.TLine(0.0,5.,9.5,5.)
mhline2.SetLineStyle(2)
mhline2.SetLineWidth(3)
mhline2.Draw("same")

#line1.Draw("same")
#line2.Draw("same")
#t3sig.Draw("same")
#t5sig.Draw("same")

outname = "plots/mh_exp_staging_varyconstr_2017.eps"
c3.SaveAs(outname)

c4 = ROOT.TCanvas("c4","c4",800,800)
c4.SetLeftMargin(0.15)
h4 = c4.DrawFrame(0,0.0,15.0,60.0)
h4.SetTitle("#delta_{CP} Resolution")
h4.GetXaxis().SetTitle("Years")
h4.GetYaxis().SetTitle("#delta_{CP} Resolution (degrees)")
h4.GetYaxis().SetTitleOffset(1.3)
h4.GetYaxis().CenterTitle()
c4.Modified()
gdiff_staged_res.SetFillColor(ROOT.kCyan+2)
gdiff_staged_res.Draw("Fsame")
gdiff_staged_res90.SetFillColor(ROOT.kPink-3)
gdiff_staged_res90.Draw("Fsame")
g_staged_res_ref.SetLineWidth(2)
g_staged_res_opt.SetLineWidth(2)
g_staged_res_ref.SetLineStyle(2)
g_staged_res_ref.Draw("same")
g_staged_res_opt.Draw("same")
g_staged_res_ref90.SetLineWidth(2)
g_staged_res_opt90.SetLineWidth(2)
g_staged_res_ref90.SetLineStyle(2)
g_staged_res_ref90.Draw("same")
g_staged_res_opt90.Draw("same")

t1res = ROOT.TPaveText(0.5,0.7,0.88,0.89,"NDC")
t1res.AddText("DUNE Sensitivity (Staged)")
t1res.AddText("Normal Ordering")
t1res.AddText("sin^{2}2#theta_{13} = 0.085 #pm 0.003")
t1res.AddText("sin^{2}#theta_{23} = 0.441 #pm 0.042")
t1res.SetBorderSize(0)
t1res.SetFillStyle(0)
t1res.SetTextAlign(12)
t1res.Draw("same")

l1res = ROOT.TLegend(0.5,0.5,0.88,0.7)
l1res.AddEntry(gdiff_staged_res90,"#delta_{CP} = -#pi/2","F")
l1res.AddEntry(gdiff_staged_res,"#delta_{CP} = 0","F")
l1res.AddEntry(g_staged_res_opt,"Nominal Analysis","L")
l1res.AddEntry(g_staged_res_ref,"#theta_{13} & #theta_{23} unconstrained","L")
l1res.SetBorderSize(0)
l1res.SetFillStyle(0)
l1res.Draw("same")

tzero = ROOT.TPaveText(10,4.0,12.3,7.0)
tzero.AddText("#delta_{CP} = 0#circ")
tzero.SetFillStyle(0)
tzero.SetBorderSize(0)
#tzero.Draw("same")

t90 = ROOT.TPaveText(10,15.0,12.5,18.0)
t90.AddText("#delta_{CP} = 90#circ")
t90.SetFillStyle(0)
t90.SetBorderSize(0)
#t90.Draw("same")

outname = "plots/resdcp_exp_staging_varyconstr_2017.eps"
c4.SaveAs(outname)
