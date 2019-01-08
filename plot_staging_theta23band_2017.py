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

xcpvlist75_ref_short = [0]
xcpvlist50_ref_short = [0]
xcpvlistbest_ref_short = [0]
xmhlist_ref_short = [0]
xmhlistbest_ref_short = [0]
xcpvlist75_ref_short_3pc = [0]
xcpvlist50_ref_short_3pc = [0]
xcpvlistbest_ref_short_3pc = [0]
xmhlist_ref_short_3pc = [0]
xmhlistbest_ref_short_3pc = [0]

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

      #Reference: Low q23
      filename = "root/sens_optimized_long_q23lo_no_exp"+str(myexp)+".root"
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

      filename = "root/sens_optimized_long_q23lo_syst3pc_no_exp"+str(myexp)+".root"
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

      #Reference: Hi q23
      filename = "root/sens_optimized_long_q23hi_no_exp"+str(myexp)+".root"
      f1 = ROOT.TFile(filename)
      xcpvgraph_short = f1.Get("CPVSig")
      xmhgraph_short = f1.Get("MHSig")
      nvals = xcpvgraph_short.GetN()
      cpv_vals = [ROOT.Double(0.0)]*nvals
      cpv_vals = array('d',cpv_vals)
      cpv_vals = xcpvgraph_short.GetY()

      mh_vals = [ROOT.Double(0.0)]*nvals
      mh_vals = array('d',mh_vals)
      mh_vals = xmhgraph_short.GetY()

      i = 0
      xcpv_vals_short = []
      xmh_vals_short = []
      while i < nvals:
            xcpv_vals_short.append(cpv_vals[i])
            xmh_vals_short.append(mh_vals[i])
            i += 1

      xcpvsig_75_short = sorted(cpv_vals_short)[24]
      xcpvsig_50_short = sorted(xcpv_vals_short)[49]
      xmhsig_100_short = min(xmh_vals_short)
      xcpvlist75_ref_short.append(xcpvsig_75_short)
      xcpvlist50_ref_short.append(xcpvsig_50_short)
      xcpvlistbest_ref_short.append(cpv_vals[26])
      xmhlist_ref_short.append(xmhsig_100_short)
      xmhlistbest_ref_short.append(mh_vals[26])
      f1.Close()

      filename = "root/sens_optimized_long_q23hi_syst3pc_no_exp"+str(myexp)+".root"
      f1 = ROOT.TFile(filename)
      xcpvgraph_short = f1.Get("CPVSig")
      xmhgraph_short = f1.Get("MHSig")
      nvals = xcpvgraph_short.GetN()
      cpv_vals = [ROOT.Double(0.0)]*nvals
      cpv_vals = array('d',cpv_vals)
      cpv_vals = xcpvgraph_short.GetY()

      mh_vals = [ROOT.Double(0.0)]*nvals
      mh_vals = array('d',mh_vals)
      mh_vals = xmhgraph_short.GetY()

      i = 0
      xcpv_vals_short = []
      xmh_vals_short = []
      while i < nvals:
            xcpv_vals_short.append(cpv_vals[i])
            xmh_vals_short.append(mh_vals[i])
            i += 1

      xcpvsig_75_short_3pc = sorted(xcpv_vals_short)[24]
      xcpvsig_50_short_3pc = sorted(xcpv_vals_short)[49]
      xmhsig_100_short_3pc = min(xmh_vals_short)
      xcpvlist75_ref_short_3pc.append(xcpvsig_75_short_3pc)
      xcpvlist50_ref_short_3pc.append(xcpvsig_50_short_3pc)
      xcpvlistbest_ref_short_3pc.append(cpv_vals[26])
      xmhlist_ref_short_3pc.append(xmhsig_100_short_3pc)
      xmhlistbest_ref_short_3pc.append(mh_vals[26])      
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
xcpvlist75_ref_short = array('d',xcpvlist75_ref_short)
cpvlist75_optimized_long = array('d',cpvlist75_optimized_long)
cpvlist75_ref_short_3pc = array('d',cpvlist75_ref_short_3pc)
xcpvlist75_ref_short_3pc = array('d',xcpvlist75_ref_short_3pc)
cpvlist75_optimized_long_3pc = array('d',cpvlist75_optimized_long_3pc)

cpvlist50_ref_short = array('d',cpvlist50_ref_short)
xcpvlist50_ref_short = array('d',xcpvlist50_ref_short)
cpvlist50_optimized_long = array('d',cpvlist50_optimized_long)
cpvlist50_ref_short_3pc = array('d',cpvlist50_ref_short_3pc)
xcpvlist50_ref_short_3pc = array('d',xcpvlist50_ref_short_3pc)
cpvlist50_optimized_long_3pc = array('d',cpvlist50_optimized_long_3pc)

cpvlistbest_ref_short = array('d',cpvlistbest_ref_short)
xcpvlistbest_ref_short = array('d',xcpvlistbest_ref_short)
cpvlistbest_optimized_long = array('d',cpvlistbest_optimized_long)
cpvlistbest_ref_short_3pc = array('d',cpvlistbest_ref_short_3pc)
xcpvlistbest_ref_short_3pc = array('d',xcpvlistbest_ref_short_3pc)
cpvlistbest_optimized_long_3pc = array('d',cpvlistbest_optimized_long_3pc)

mhlist_ref_short = array('d',mhlist_ref_short)
xmhlist_ref_short = array('d',xmhlist_ref_short)
mhlist_optimized_long = array('d',mhlist_optimized_long)
mhlist_ref_short_3pc = array('d',mhlist_ref_short_3pc)
xmhlist_ref_short_3pc = array('d',xmhlist_ref_short_3pc)
mhlist_optimized_long_3pc = array('d',mhlist_optimized_long_3pc)

mhlistbest_ref_short = array('d',mhlistbest_ref_short)
xmhlistbest_ref_short = array('d',xmhlistbest_ref_short)
mhlistbest_optimized_long = array('d',mhlistbest_optimized_long)
mhlistbest_ref_short_3pc = array('d',mhlistbest_ref_short_3pc)
xmhlistbest_ref_short_3pc = array('d',xmhlistbest_ref_short_3pc)
mhlistbest_optimized_long_3pc = array('d',mhlistbest_optimized_long_3pc)

g_cpvsig_75_ref_short = ROOT.TGraph(n,explist,cpvlist75_ref_short)
xg_cpvsig_75_ref_short = ROOT.TGraph(n,explist,xcpvlist75_ref_short)
g_cpvsig_75_optimized_long = ROOT.TGraph(n,explist,cpvlist75_optimized_long)
g_cpvsig_75_ref_short_3pc = ROOT.TGraph(n,explist,cpvlist75_ref_short_3pc)
xg_cpvsig_75_ref_short_3pc = ROOT.TGraph(n,explist,xcpvlist75_ref_short_3pc)
g_cpvsig_75_optimized_long_3pc = ROOT.TGraph(n,explist,cpvlist75_optimized_long_3pc)

g_cpvsig_50_ref_short = ROOT.TGraph(n,explist,cpvlist50_ref_short)
xg_cpvsig_50_ref_short = ROOT.TGraph(n,explist,xcpvlist50_ref_short)
g_cpvsig_50_optimized_long = ROOT.TGraph(n,explist,cpvlist50_optimized_long)
g_cpvsig_50_ref_short_3pc = ROOT.TGraph(n,explist,cpvlist50_ref_short_3pc)
xg_cpvsig_50_ref_short_3pc = ROOT.TGraph(n,explist,xcpvlist50_ref_short_3pc)
g_cpvsig_50_optimized_long_3pc = ROOT.TGraph(n,explist,cpvlist50_optimized_long_3pc)

g_cpvsigbest_ref_short = ROOT.TGraph(n,explist,cpvlistbest_ref_short)
xg_cpvsigbest_ref_short = ROOT.TGraph(n,explist,xcpvlistbest_ref_short)
g_cpvsigbest_optimized_long = ROOT.TGraph(n,explist,cpvlistbest_optimized_long)
g_cpvsigbest_ref_short_3pc = ROOT.TGraph(n,explist,cpvlistbest_ref_short_3pc)
xg_cpvsigbest_ref_short_3pc = ROOT.TGraph(n,explist,xcpvlistbest_ref_short_3pc)
g_cpvsigbest_optimized_long_3pc = ROOT.TGraph(n,explist,cpvlistbest_optimized_long_3pc)

g_mhsig_100_ref_short = ROOT.TGraph(n,explist,mhlist_ref_short)
xg_mhsig_100_ref_short = ROOT.TGraph(n,explist,xmhlist_ref_short)
g_mhsig_100_optimized_long = ROOT.TGraph(n,explist,mhlist_optimized_long)
g_mhsig_100_ref_short_3pc = ROOT.TGraph(n,explist,mhlist_ref_short_3pc)
xg_mhsig_100_ref_short_3pc = ROOT.TGraph(n,explist,xmhlist_ref_short_3pc)
g_mhsig_100_optimized_long_3pc = ROOT.TGraph(n,explist,mhlist_optimized_long_3pc)

g_mhsigbest_ref_short = ROOT.TGraph(n,explist,mhlistbest_ref_short)
xg_mhsigbest_ref_short = ROOT.TGraph(n,explist,xmhlistbest_ref_short)
g_mhsigbest_optimized_long = ROOT.TGraph(n,explist,mhlistbest_optimized_long)
g_mhsigbest_ref_short_3pc = ROOT.TGraph(n,explist,mhlistbest_ref_short_3pc)
xg_mhsigbest_ref_short_3pc = ROOT.TGraph(n,explist,xmhlistbest_ref_short_3pc)
g_mhsigbest_optimized_long_3pc = ROOT.TGraph(n,explist,mhlistbest_optimized_long_3pc)

g_cpvsig_75_ref_short.SetLineWidth(3)
xg_cpvsig_75_ref_short.SetLineWidth(3)
g_cpvsig_75_ref_short_3pc.SetLineWidth(3)
xg_cpvsig_75_ref_short_3pc.SetLineWidth(3)
g_cpvsig_75_optimized_long.SetLineWidth(3)
g_cpvsig_75_optimized_long_3pc.SetLineWidth(3)
g_cpvsig_75_ref_short.SetLineColor(ROOT.kBlue-1)
xg_cpvsig_75_ref_short.SetLineColor(ROOT.kBlue-1)
g_cpvsig_75_ref_short_3pc.SetLineColor(ROOT.kBlue-1)
xg_cpvsig_75_ref_short_3pc.SetLineColor(ROOT.kBlue-1)
g_cpvsig_75_optimized_long.SetLineColor(ROOT.kGreen-1)
g_cpvsig_75_optimized_long_3pc.SetLineColor(ROOT.kGreen-1)

g_cpvsig_50_ref_short.SetLineWidth(3)
xg_cpvsig_50_ref_short.SetLineWidth(3)
g_cpvsig_50_ref_short_3pc.SetLineWidth(3)
xg_cpvsig_50_ref_short_3pc.SetLineWidth(3)
g_cpvsig_50_optimized_long.SetLineWidth(3)
g_cpvsig_50_optimized_long_3pc.SetLineWidth(3)
g_cpvsig_50_ref_short.SetLineColor(ROOT.kBlue-1)
xg_cpvsig_50_ref_short.SetLineColor(ROOT.kBlue-1)
g_cpvsig_50_ref_short_3pc.SetLineColor(ROOT.kBlue-1)
xg_cpvsig_50_ref_short_3pc.SetLineColor(ROOT.kBlue-1)
g_cpvsig_50_optimized_long.SetLineColor(ROOT.kGreen-1)
g_cpvsig_50_optimized_long_3pc.SetLineColor(ROOT.kGreen-1)

g_cpvsigbest_ref_short.SetLineWidth(3)
xg_cpvsigbest_ref_short.SetLineWidth(3)
g_cpvsigbest_ref_short_3pc.SetLineWidth(3)
xg_cpvsigbest_ref_short_3pc.SetLineWidth(3)
g_cpvsigbest_optimized_long.SetLineWidth(3)
g_cpvsigbest_optimized_long_3pc.SetLineWidth(3)
g_cpvsigbest_ref_short.SetLineColor(ROOT.kBlue-1)
xg_cpvsigbest_ref_short.SetLineColor(ROOT.kBlue-1)
g_cpvsigbest_ref_short_3pc.SetLineColor(ROOT.kBlue-1)
xg_cpvsigbest_ref_short_3pc.SetLineColor(ROOT.kBlue-1)
g_cpvsigbest_optimized_long.SetLineColor(ROOT.kGreen-1)
g_cpvsigbest_optimized_long_3pc.SetLineColor(ROOT.kGreen-1)

g_mhsig_100_ref_short.SetLineWidth(3)
xg_mhsig_100_ref_short.SetLineWidth(3)
g_mhsig_100_ref_short_3pc.SetLineWidth(3)
xg_mhsig_100_ref_short_3pc.SetLineWidth(3)
g_mhsig_100_optimized_long.SetLineWidth(3)
g_mhsig_100_optimized_long_3pc.SetLineWidth(3)
g_mhsig_100_ref_short.SetLineColor(ROOT.kBlue-1)
xg_mhsig_100_ref_short.SetLineColor(ROOT.kBlue-1)
g_mhsig_100_ref_short_3pc.SetLineColor(ROOT.kBlue-1)
xg_mhsig_100_ref_short_3pc.SetLineColor(ROOT.kBlue-1)
g_mhsig_100_optimized_long.SetLineColor(ROOT.kGreen-1)
g_mhsig_100_optimized_long_3pc.SetLineColor(ROOT.kGreen-1)

g_mhsigbest_ref_short.SetLineWidth(3)
xg_mhsigbest_ref_short.SetLineWidth(3)
g_mhsigbest_ref_short_3pc.SetLineWidth(3)
xg_mhsigbest_ref_short_3pc.SetLineWidth(3)
g_mhsigbest_optimized_long.SetLineWidth(3)
g_mhsigbest_optimized_long_3pc.SetLineWidth(3)
g_mhsigbest_ref_short.SetLineColor(ROOT.kBlue-1)
xg_mhsigbest_ref_short.SetLineColor(ROOT.kBlue-1)
g_mhsigbest_ref_short_3pc.SetLineColor(ROOT.kBlue-1)
xg_mhsigbest_ref_short_3pc.SetLineColor(ROOT.kBlue-1)
g_mhsigbest_optimized_long.SetLineColor(ROOT.kGreen-1)
g_mhsigbest_optimized_long_3pc.SetLineColor(ROOT.kGreen-1)

# #Get resolutions
r1 = ROOT.TFile("root/resdcp0_optimized_long_no.root")
g_res_nom = r1.Get("Res")
r2 = ROOT.TFile("root/resdcp0_optimized_long_q23lo_no.root")
g_res_q23lo = r2.Get("Res")
r3 = ROOT.TFile("root/resdcp0_optimized_long_q23hi_no.root")
g_res_q23hi = r3.Get("Res")
r4 = ROOT.TFile("root/resdcp0_optimized_long_syst3pc_no.root")
g_res_nom_3pc = r4.Get("Res")
r5 = ROOT.TFile("root/resdcp0_optimized_long_q23lo_syst3pc_no.root")
g_res_q23lo_3pc = r5.Get("Res")
r6 = ROOT.TFile("root/resdcp0_optimized_long_q23hi_syst3pc_no.root")
g_res_q23hi_3pc = r6.Get("Res")

r190 = ROOT.TFile("root/resdcp-90_optimized_long_no.root")
g_res90_nom = r190.Get("Res")
r290 = ROOT.TFile("root/resdcp-90_optimized_long_q23lo_no.root")
g_res90_q23lo = r290.Get("Res")
r390 = ROOT.TFile("root/resdcp-90_optimized_long_q23hi_no.root")
g_res90_q23hi = r390.Get("Res")
r490 = ROOT.TFile("root/resdcp-90_optimized_long_syst3pc_no.root")
g_res90_nom_3pc = r490.Get("Res")
r590 = ROOT.TFile("root/resdcp-90_optimized_long_q23lo_syst3pc_no.root")
g_res90_q23lo_3pc = r590.Get("Res")
r690 = ROOT.TFile("root/resdcp-90_optimized_long_q23hi_syst3pc_no.root")
g_res90_q23hi_3pc = r690.Get("Res")


years = [0,0.25,0.5,0.75,1,1.25,1.5,2,2.5,3,3.5,4,4.5,5,6,7,8,9,10,11,12,13,14,15]
cpv75_ref = [0]
xcpv75_ref = [0]
cpv50_ref = [0]
xcpv50_ref = [0]
cpvbest_ref = [0]
xcpvbest_ref = [0]
mh_ref = [0]
xmh_ref = [0]
mhbest_ref = [0]
xmhbest_ref = [0]
res_nom = [999]
res90_nom = [999]
cpv75_opt = [0]
cpv50_opt = [0]
cpvbest_opt = [0]
mh_opt = [0]
mhbest_opt = [0]
res_q23lo = [999]
res90_q23lo = [999]
res_q23hi = [999]
res90_q23hi = [999]


def fillstaged(thisexp,syst=""):
      thing = globals()["g_cpvsig_75_ref_short"+syst]
      cpv75_ref.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["xg_cpvsig_75_ref_short"+syst]
      xcpv75_ref.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["g_cpvsig_50_ref_short"+syst]
      cpv50_ref.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["xg_cpvsig_50_ref_short"+syst]
      xcpv50_ref.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["g_cpvsigbest_ref_short"+syst]
      cpvbest_ref.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["xg_cpvsigbest_ref_short"+syst]
      xcpvbest_ref.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["g_mhsig_100_ref_short"+syst]
      mh_ref.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["xg_mhsig_100_ref_short"+syst]
      xmh_ref.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["g_mhsigbest_ref_short"+syst]
      mhbest_ref.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["xg_mhsigbest_ref_short"+syst]
      xmhbest_ref.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["g_res_nom"+syst]
      res_nom.append(thing.Eval(thisexp,0,""))
      thing = globals()["g_res90_nom"+syst]
      res90_nom.append(thing.Eval(thisexp,0,""))
      thing = globals()["g_res_q23lo"+syst]
      res_q23lo.append(thing.Eval(thisexp,0,""))
      thing = globals()["g_res90_q23lo"+syst]
      res90_q23lo.append(thing.Eval(thisexp,0,""))
      thing = globals()["g_res_q23hi"+syst]
      res_q23hi.append(thing.Eval(thisexp,0,""))
      thing = globals()["g_res90_q23hi"+syst]
      res90_q23hi.append(thing.Eval(thisexp,0,""))
      thing = globals()["g_cpvsig_75_optimized_long"+syst]
      cpv75_opt.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["g_cpvsig_50_optimized_long"+syst]
      cpv50_opt.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["g_cpvsigbest_optimized_long"+syst]
      cpvbest_opt.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["g_mhsig_100_optimized_long"+syst]
      mh_opt.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["g_mhsigbest_optimized_long"+syst]
      mhbest_opt.append(g_mhsigbest_optimized_long_3pc.Eval(thisexp,0,"S"))
      
      return 0

g_staging = ROOT.TGraph()
g_staging.SetPoint(0, 0.0, 0.0)
#Year 0.25: 20kt * 1.07 MW, 3% syst = 5.35 kt-MW-yr
thisexp = 5.35
print "Year 0.25: ", thisexp
fillstaged(thisexp,"_3pc")
g_staging.SetPoint(g_staging.GetN(),thisexp, years[g_staging.GetN()])

#Year 0.5: 20kt * 1.07 MW, 3% syst = 10.7 kt-MW-yr
thisexp = 10.7
print "Year 0.5: ", thisexp
fillstaged(thisexp,"_3pc")
g_staging.SetPoint(g_staging.GetN(),thisexp, years[g_staging.GetN()])

#Year 0.75: 20kt * 1.07 MW, 3% syst = 16.05 kt-MW-yr
thisexp = 16.05
print "Year 0.75: ", thisexp
fillstaged(thisexp,"_3pc")
g_staging.SetPoint(g_staging.GetN(),thisexp, years[g_staging.GetN()])

#Year 1: 20kt * 1.07 MW, 3% syst = 21.4 kt-MW-yr
thisexp = 21.4
print "Year 1: ", thisexp
fillstaged(thisexp,"_3pc")
g_staging.SetPoint(g_staging.GetN(),thisexp, years[g_staging.GetN()])

#Year 1.25: + 30kt * 1.07 MW, 3% syst = 53.5 kt-MW-yr
thisexp += 30*1.07*0.25
print "Year 1.25: ", thisexp
fillstaged(thisexp,"_3pc")
g_staging.SetPoint(g_staging.GetN(),thisexp, years[g_staging.GetN()])

#Year 1.5: + 30kt * 1.07 MW, 3% syst = 53.5 kt-MW-yr
thisexp += 30*1.07*0.25
print "Year 1.5: ", thisexp
fillstaged(thisexp,"_3pc")
g_staging.SetPoint(g_staging.GetN(),thisexp, years[g_staging.GetN()])

#Year 2: + 30kt * 1.07 MW, 3% syst = 53.5 kt-MW-yr
thisexp += 30*1.07*0.5
print "Year 2: ", thisexp
fillstaged(thisexp,"_3pc")
g_staging.SetPoint(g_staging.GetN(),thisexp, years[g_staging.GetN()])

#Year 2.5: + 30kt * 1.07 MW, 3% syst = 53.5 kt-MW-yr
thisexp += 30*1.07*0.5
print "Year 2.5: ", thisexp
fillstaged(thisexp,"_3pc")
g_staging.SetPoint(g_staging.GetN(),thisexp, years[g_staging.GetN()])

#Year 3: + 30kt * 1.07 MW, 3% syst = 85.6 kt-MW-yr
thisexp += 30*1.07*0.5
print "Year 3: ", thisexp
fillstaged(thisexp,"_3pc")
g_staging.SetPoint(g_staging.GetN(),thisexp, years[g_staging.GetN()])

#Year 3.5: + 40kt * 1.07 MW, 2% syst 
thisexp += 40*1.07*0.5
print "Year 3.5: ", thisexp
fillstaged(thisexp)
g_staging.SetPoint(g_staging.GetN(),thisexp, years[g_staging.GetN()])

#Year 4: + 40kt * 1.07 MW, 2% syst = 128.4 kt-MW-yr
thisexp += 40*1.07*0.5
print "Year 4: ", thisexp
fillstaged(thisexp)
g_staging.SetPoint(g_staging.GetN(),thisexp, years[g_staging.GetN()])

#Year 4.5: + 40kt * 1.07 MW, 2% syst = 171.2 kt-MW-yr
thisexp += 40*1.07*0.5
print "Year 4.5: ", thisexp
fillstaged(thisexp)
g_staging.SetPoint(g_staging.GetN(),thisexp, years[g_staging.GetN()])

#Year 5: + 40kt * 1.07 MW, 2% syst = 171.2 kt-MW-yr
thisexp += 40*1.07*0.5
print "Year 5: ", thisexp
fillstaged(thisexp)
g_staging.SetPoint(g_staging.GetN(),thisexp, years[g_staging.GetN()])

#Year 6: + 40kt * 1.07 MW, 2% syst = 214 kt-MW-yr
thisexp += 40*1.07
print "Year 6: ", thisexp
fillstaged(thisexp)
g_staging.SetPoint(g_staging.GetN(),thisexp, years[g_staging.GetN()])

#Year 7: + 40kt * 2.14 MW, 2% syst = 299.6 kt-MW-yr
thisexp += 40*2.14
print "Year 7: ", thisexp
fillstaged(thisexp)
g_staging.SetPoint(g_staging.GetN(),thisexp, years[g_staging.GetN()])

#Year 8: + 40kt * 2.14 MW, 2% syst
thisexp += 40*2.14
print "Year 8: ", thisexp
fillstaged(thisexp)
g_staging.SetPoint(g_staging.GetN(),thisexp, years[g_staging.GetN()])

#Year 9: + 40kt * 2.14 MW, 2% syst
thisexp += 40*2.14
print "Year 9: ", thisexp
fillstaged(thisexp)
g_staging.SetPoint(g_staging.GetN(),thisexp, years[g_staging.GetN()])

#Year 10: + 40kt * 2.14 MW, 2% syst
thisexp += 40*2.14
print "Year 10: ", thisexp
fillstaged(thisexp)
g_staging.SetPoint(g_staging.GetN(),thisexp, years[g_staging.GetN()])

#Year 11: + 40kt * 2.14 MW, 2% syst
thisexp += 40*2.14
print "Year 11: ", thisexp
fillstaged(thisexp)
g_staging.SetPoint(g_staging.GetN(),thisexp, years[g_staging.GetN()])

#Year 12: + 40kt * 2.14 MW, 2% syst
thisexp += 40*2.14
print "Year 12: ", thisexp
fillstaged(thisexp)
g_staging.SetPoint(g_staging.GetN(),thisexp, years[g_staging.GetN()])

#Year 13: + 40kt * 2.14 MW, 2% syst
thisexp += 40*2.14
print "Year 13: ", thisexp
fillstaged(thisexp)
g_staging.SetPoint(g_staging.GetN(),thisexp, years[g_staging.GetN()])

#Year 14: + 40kt * 2.14 MW, 2% syst
thisexp += 40*2.14
print "Year 14: ", thisexp
fillstaged(thisexp)
g_staging.SetPoint(g_staging.GetN(),thisexp, years[g_staging.GetN()])

#Year 15: + 40kt * 2.14 MW, 2% syst
thisexp += 40*2.14
print "Year 15: ", thisexp
fillstaged(thisexp)
g_staging.SetPoint(g_staging.GetN(),thisexp, years[g_staging.GetN()])

f_out = ROOT.TFile("root/staging_convert.root","RECREATE")
g_staging.SetName("g_exp")
g_staging.Write()
f_out.Close()

nyears = len(years)
years = array('d',years)
cpv75_ref = array('d',cpv75_ref)
xcpv75_ref = array('d',xcpv75_ref)
cpv50_ref = array('d',cpv50_ref)
xcpv50_ref = array('d',xcpv50_ref)
cpvbest_ref = array('d',cpvbest_ref)
xcpvbest_ref = array('d',xcpvbest_ref)
mh_ref = array('d',mh_ref)
xmh_ref = array('d',xmh_ref)
mhbest_ref = array('d',mhbest_ref)
xmhbest_ref = array('d',xmhbest_ref)
res_nom = array('d',res_nom)
res_q23lo = array('d',res_q23lo)
res_q23hi = array('d',res_q23hi)
res90_nom = array('d',res90_nom)
res90_q23lo = array('d',res90_q23lo)
res90_q23hi = array('d',res90_q23hi)
cpv75_opt = array('d',cpv75_opt)
cpv50_opt = array('d',cpv50_opt)
cpvbest_opt = array('d',cpvbest_opt)
mh_opt = array('d',mh_opt)
mhbest_opt = array('d',mhbest_opt)

g_staged_cpv75_ref = ROOT.TGraph(nyears,years,cpv75_ref)
xg_staged_cpv75_ref = ROOT.TGraph(nyears,years,xcpv75_ref)
g_staged_cpv50_ref = ROOT.TGraph(nyears,years,cpv50_ref)
xg_staged_cpv50_ref = ROOT.TGraph(nyears,years,xcpv50_ref)
g_staged_cpvbest_ref = ROOT.TGraph(nyears,years,cpvbest_ref)
xg_staged_cpvbest_ref = ROOT.TGraph(nyears,years,xcpvbest_ref)
g_staged_mh_ref = ROOT.TGraph(nyears,years,mh_ref)
xg_staged_mh_ref = ROOT.TGraph(nyears,years,xmh_ref)
g_staged_mhbest_ref = ROOT.TGraph(nyears,years,mhbest_ref)
xg_staged_mhbest_ref = ROOT.TGraph(nyears,years,xmhbest_ref)
g_staged_res_nom = ROOT.TGraph(nyears,years,res_nom)
g_staged_res_q23lo = ROOT.TGraph(nyears,years,res_q23lo)
g_staged_res_q23hi = ROOT.TGraph(nyears,years,res_q23hi)
g_staged_res90_nom = ROOT.TGraph(nyears,years,res90_nom)
g_staged_res90_q23lo = ROOT.TGraph(nyears,years,res90_q23lo)
g_staged_res90_q23hi = ROOT.TGraph(nyears,years,res90_q23hi)
g_staged_cpv75_opt = ROOT.TGraph(nyears,years,cpv75_opt)
g_staged_cpv50_opt = ROOT.TGraph(nyears,years,cpv50_opt)
g_staged_cpvbest_opt = ROOT.TGraph(nyears,years,cpvbest_opt)
g_staged_mh_opt = ROOT.TGraph(nyears,years,mh_opt)
g_staged_mhbest_opt = ROOT.TGraph(nyears,years,mhbest_opt)

gdiff_staged_cpv75 = filldiff(g_staged_cpv75_ref,xg_staged_cpv75_ref)
gdiff_staged_cpv50 = filldiff(g_staged_cpv50_ref,xg_staged_cpv50_ref)
gdiff_staged_cpvbest = filldiff(g_staged_cpvbest_ref,xg_staged_cpvbest_ref)
gdiff_staged_mh = filldiff(xg_staged_mh_ref,g_staged_mh_ref)
gdiff_staged_mhbest = filldiff(xg_staged_mhbest_ref,g_staged_mhbest_ref)
gdiff_staged_res = filldiff(g_staged_res_q23hi,g_staged_res_q23lo)
gdiff_staged_res90 = filldiff(g_staged_res90_q23hi,g_staged_res90_q23lo)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0,0.0,15.0,15.0)
h1.SetTitle("CP Violation Sensitivity")
h1.GetXaxis().SetTitle("Years")
h1.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h1.GetYaxis().SetTitleOffset(1.5)
h1.GetYaxis().CenterTitle()
c1.Modified()

gdiff_staged_cpv75.SetFillColor(ROOT.kCyan+2)
g_staged_cpv75_opt.SetLineWidth(3)
g_staged_cpv75_opt.SetLineStyle(2)

gdiff_staged_cpv75.Draw("F same")
g_staged_cpv75_opt.Draw("same")

gdiff_staged_cpv50.SetFillColor(ROOT.kCyan-7)
g_staged_cpv50_opt.SetLineWidth(3)
g_staged_cpv50_opt.SetLineStyle(2)

gdiff_staged_cpv50.Draw("F same")
g_staged_cpv50_opt.Draw("same")

gdiff_staged_cpvbest.SetFillColor(ROOT.kPink-3)
g_staged_cpvbest_opt.SetLineWidth(3)
g_staged_cpvbest_opt.SetLineStyle(2)

gdiff_staged_cpvbest.Draw("F same")
g_staged_cpvbest_opt.Draw("same")

t1 = ROOT.TPaveText(0.16,0.75,0.51,0.89,"NDC")
t1.AddText("DUNE Sensitivity (Staged)")
t1.AddText("Normal Ordering")
t1.AddText("sin^{2}2#theta_{13} = 0.085 #pm 0.003")
t1.AddText("#theta_{23}: NuFit 2016 (90% C.L. range)")
t1.SetBorderSize(0)
#t1.SetFillStyle(0)
t1.SetFillColor(ROOT.kWhite)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.55,0.72,0.89,0.89)
l1.AddEntry(gdiff_staged_cpvbest, "#delta_{CP} = -#pi/2","F")
l1.AddEntry(gdiff_staged_cpv50, "50% of #delta_{CP} values","F")
l1.AddEntry(gdiff_staged_cpv75, "75% of #delta_{CP} values","F")
l1.AddEntry(g_staged_cpv50_opt,"sin^{2}#theta_{23} = 0.441 #pm 0.042", "L")
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

outname = "plots/cpv_exp_staging_th23band_2017.eps"
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
g_staged_mh_opt.SetLineWidth(3)
g_staged_mh_opt.SetLineStyle(2)

gdiff_staged_mh.Draw("F same")
g_staged_mh_opt.Draw("same")

gdiff_staged_mhbest.SetFillColor(ROOT.kPink-3)
g_staged_mhbest_opt.SetLineWidth(3)
g_staged_mhbest_opt.SetLineStyle(2)

gdiff_staged_mhbest.Draw("F same")
g_staged_mhbest_opt.Draw("same")

t1.Draw("same")

lm1 = ROOT.TLegend(0.55,0.79,0.88,0.89)
lm1.AddEntry(gdiff_staged_mhbest, "#delta_{CP} = -#pi/2","F")
lm1.AddEntry(gdiff_staged_mh, "100% of #delta_{CP} values","F")
lm1.AddEntry(g_staged_mh_opt,"sin^{2}#theta_{23} = 0.441 #pm 0.042", "L")      
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

outname = "plots/mh_exp_staging_th23band_2017.eps"
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
g_staged_res_nom.SetLineWidth(2)
g_staged_res90_nom.SetLineWidth(2)
g_staged_res_nom.SetLineStyle(2)
g_staged_res90_nom.SetLineStyle(2)

g_staged_res_nom.Draw("same")
g_staged_res90_nom.Draw("same")

t1res = ROOT.TPaveText(0.5,0.7,0.88,0.89,"NDC")
t1res.AddText("DUNE Sensitivity (Staged)")
t1res.AddText("Normal Ordering")
t1res.AddText("sin^{2}2#theta_{13} = 0.085 #pm 0.003")
t1res.AddText("#theta_{23}: NuFit 2016 (90% C.L. range)")
t1res.SetBorderSize(0)
t1res.SetFillStyle(0)
t1res.SetTextAlign(12)
t1res.Draw("same")

l1res = ROOT.TLegend(0.5,0.5,0.88,0.7)
l1res.AddEntry(gdiff_staged_res90,"#delta_{CP} = -#pi/2","F")
l1res.AddEntry(gdiff_staged_res,"#delta_{CP} = 0","F")
l1res.AddEntry(g_staged_res_nom,"sin^{2}#theta_{23} = 0.441 #pm 0.042", "L")
l1res.SetBorderSize(0)
l1res.SetFillStyle(0)
l1res.Draw("same")

outname = "plots/resdcp_exp_staging_th23band_2017.eps"
c4.SaveAs(outname)
