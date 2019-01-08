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

explist = [10,28,50,100,200,300,400,600,800,1000,1250,1500]
cpvlist75_ref_short = []
cpvlist50_ref_short = []
cpvlistmax_ref_short = []
cpvlistmaxpos_ref_short = []
mhlist_ref_short = []
mhlist50_ref_short = []
mhlist0_ref_short = []

cpvlist50_optimized_long = []
cpvlist75_optimized_long = []
cpvlistmax_optimized_long = []
cpvlistmaxpos_optimized_long = []
mhlist_optimized_long = []
mhlist50_optimized_long = []
mhlist0_optimized_long = []

for myexp in explist:

      #Reference: Short pipe
      filename = "root/sens_enhanced_short_exp"+str(myexp)+".root"
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
      mhsig_50_short = sorted(mh_vals_short)[49]
      mhsig_0_short = max(mh_vals_short)
      cpvlist75_ref_short.append(cpvsig_75_short)
      cpvlist50_ref_short.append(cpvsig_50_short)
      cpvlistmax_ref_short.append(cpv_vals_short[25])
      cpvlistmaxpos_ref_short.append(cpv_vals_short[74])
      mhlist_ref_short.append(mhsig_100_short)
      mhlist50_ref_short.append(mhsig_50_short)
      mhlist0_ref_short.append(mhsig_0_short)
      f1.Close()

      
      #Optimized long
      filename = "root/sens_optimized_long_exp"+str(myexp)+".root"
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
      mhsig_50_optimized_long = sorted(mh_vals_optimized_long)[49]
      mhsig_0_optimized_long = max(mh_vals_optimized_long)
      cpvlist75_optimized_long.append(cpvsig_75_optimized_long)
      cpvlist50_optimized_long.append(cpvsig_50_optimized_long)
      cpvlistmax_optimized_long.append(cpv_vals_optimized_long[25])
      cpvlistmaxpos_optimized_long.append(cpv_vals_optimized_long[74])
      mhlist_optimized_long.append(mhsig_100_optimized_long)
      mhlist50_optimized_long.append(mhsig_50_optimized_long)
      mhlist0_optimized_long.append(mhsig_0_optimized_long)
      f1.Close()

n = len(explist)
explist = array('d',explist)
cpvlist75_ref_short = array('d',cpvlist75_ref_short)
cpvlist75_optimized_long = array('d',cpvlist75_optimized_long)

cpvlist50_ref_short = array('d',cpvlist50_ref_short)
cpvlist50_optimized_long = array('d',cpvlist50_optimized_long)

mhlist_ref_short = array('d',mhlist_ref_short)
mhlist_optimized_long = array('d',mhlist_optimized_long)

mhlist50_ref_short = array('d',mhlist50_ref_short)
mhlist50_optimized_long = array('d',mhlist50_optimized_long)

mhlist0_ref_short = array('d',mhlist0_ref_short)
mhlist0_optimized_long = array('d',mhlist0_optimized_long)

cpvlistmax_ref_short = array('d',cpvlistmax_ref_short)
cpvlistmax_optimized_long = array('d',cpvlistmax_optimized_long)

cpvlistmaxpos_ref_short = array('d',cpvlistmaxpos_ref_short)
cpvlistmaxpos_optimized_long = array('d',cpvlistmaxpos_optimized_long)

f1 = ROOT.TFile("root/resdcp0_enhanced_short.root")
res_ref = f1.Get("Res")
nres = res_ref.GetN()
myexpvals = [ROOT.Double(0.0)]*nvals
mycpvvals = [ROOT.Double(0.0)]*nvals
myexpvals = array('d',myexpvals)
mycpvvals = array('d',mycpvvals)
myexpvals = res_ref.GetX()
mycpvvals = res_ref.GetY()
g_res_ref = ROOT.TGraph(nres,mycpvvals,myexpvals)


f2 = ROOT.TFile("root/resdcp0_optimized_long.root")
res_opt = f2.Get("Res")
nres = res_opt.GetN()
myexpvals = [ROOT.Double(0.0)]*nvals
mycpvvals = [ROOT.Double(0.0)]*nvals
myexpvals = array('d',myexpvals)
mycpvvals = array('d',mycpvvals)
myexpvals = res_opt.GetX()
mycpvvals = res_opt.GetY()
g_res_opt = ROOT.TGraph(nres,mycpvvals,myexpvals)

f3 = ROOT.TFile("root/resdcp90_enhanced_short.root")
res_ref90 = f3.Get("Res")

f4 = ROOT.TFile("root/resdcp90_optimized_long.root")
res_opt90 = f4.Get("Res")

f5 = ROOT.TFile("root/resdcp-90_enhanced_short.root")
res_ref90neg = f5.Get("Res")

f6 = ROOT.TFile("root/resdcp-90_optimized_long.root")
res_opt90neg = f6.Get("Res")

f7 = ROOT.TFile("root/resth23_enhanced_short.root")
resth23_ref = f7.Get("Res")
nres = resth23_ref.GetN()
myexpvals = [ROOT.Double(0.0)]*nvals
mycpvvals = [ROOT.Double(0.0)]*nvals
myexpvals = array('d',myexpvals)
mycpvvals = array('d',mycpvvals)
myexpvals = resth23_ref.GetX()
mycpvvals = resth23_ref.GetY()
g_resth23_ref = ROOT.TGraph(nres,mycpvvals,myexpvals)


f8 = ROOT.TFile("root/resth23_optimized_long.root")
resth23_opt = f8.Get("Res")
nres = resth23_opt.GetN()
myexpvals = [ROOT.Double(0.0)]*nvals
mycpvvals = [ROOT.Double(0.0)]*nvals
myexpvals = array('d',myexpvals)
mycpvvals = array('d',mycpvvals)
myexpvals = resth23_opt.GetX()
mycpvvals = resth23_opt.GetY()
g_resth23_opt = ROOT.TGraph(nres,mycpvvals,myexpvals)

f9 = ROOT.TFile("root/resth13_enhanced_short.root")
resth13_ref = f9.Get("Res")
nres = resth13_ref.GetN()
myexpvals = [ROOT.Double(0.0)]*nvals
mycpvvals = [ROOT.Double(0.0)]*nvals
myexpvals = array('d',myexpvals)
mycpvvals = array('d',mycpvvals)
myexpvals = resth13_ref.GetX()
mycpvvals = resth13_ref.GetY()
g_resth13_ref = ROOT.TGraph(nres,mycpvvals,myexpvals)

f10 = ROOT.TFile("root/resth13_optimized_long.root")
resth13_opt = f10.Get("Res")
nres = resth13_opt.GetN()
myexpvals = [ROOT.Double(0.0)]*nvals
mycpvvals = [ROOT.Double(0.0)]*nvals
myexpvals = array('d',myexpvals)
mycpvvals = array('d',mycpvvals)
myexpvals = resth13_opt.GetX()
mycpvvals = resth13_opt.GetY()
g_resth13_opt = ROOT.TGraph(nres,mycpvvals,myexpvals)


#Fill exposure graphs backwards
g_cpvsig_75_ref_short = ROOT.TGraph(n,cpvlist75_ref_short,explist)
g_cpvsig_75_optimized_long = ROOT.TGraph(n,cpvlist75_optimized_long,explist)

g_cpvsig_50_ref_short = ROOT.TGraph(n,cpvlist50_ref_short,explist)
g_cpvsig_50_optimized_long = ROOT.TGraph(n,cpvlist50_optimized_long,explist)

g_mhsig_ref_short = ROOT.TGraph(n,mhlist_ref_short,explist)
g_mhsig_optimized_long = ROOT.TGraph(n,mhlist_optimized_long,explist)

g_mhsig50_ref_short = ROOT.TGraph(n,mhlist50_ref_short,explist)
g_mhsig50_optimized_long = ROOT.TGraph(n,mhlist50_optimized_long,explist)

g_mhsig0_ref_short = ROOT.TGraph(n,mhlist0_ref_short,explist)
g_mhsig0_optimized_long = ROOT.TGraph(n,mhlist0_optimized_long,explist)

g_cpvmax_ref_short = ROOT.TGraph(n,cpvlistmax_ref_short,explist)
g_cpvmax_optimized_long = ROOT.TGraph(n,cpvlistmax_optimized_long,explist)

g_cpvmaxpos_ref_short = ROOT.TGraph(n,cpvlistmaxpos_ref_short,explist)
g_cpvmaxpos_optimized_long = ROOT.TGraph(n,cpvlistmaxpos_optimized_long,explist)

#Get numbers I want

cpv75_ref_exp = g_cpvsig_75_ref_short.Eval(3.0,0,"S")
cpv75_opt_exp = g_cpvsig_75_optimized_long.Eval(3.0,0,"S")

cpv50_ref_exp = g_cpvsig_50_ref_short.Eval(5.0,0,"S")
cpv50_opt_exp = g_cpvsig_50_optimized_long.Eval(5.0,0,"S")

cpvmax_ref_exp = g_cpvmax_ref_short.Eval(3.0,0,"S")
cpvmax_opt_exp = g_cpvmax_optimized_long.Eval(3.0,0,"S")

cpvmaxpos_ref_exp = g_cpvmaxpos_ref_short.Eval(3.0,0,"S")
cpvmaxpos_opt_exp = g_cpvmaxpos_optimized_long.Eval(3.0,0,"S")

cpvmax5s_ref_exp = g_cpvmax_ref_short.Eval(5.0,0,"S")
cpvmax5s_opt_exp = g_cpvmax_optimized_long.Eval(5.0,0,"S")

cpvmaxpos5s_ref_exp = g_cpvmaxpos_ref_short.Eval(5.0,0,"S")
cpvmaxpos5s_opt_exp = g_cpvmaxpos_optimized_long.Eval(5.0,0,"S")

mh_ref_exp = g_mhsig_ref_short.Eval(5.0,0,"S")
mh_opt_exp = g_mhsig_optimized_long.Eval(5.0,0,"S")

mh50_ref_exp = g_mhsig50_ref_short.Eval(5.0,0,"S")
mh50_opt_exp = g_mhsig50_optimized_long.Eval(5.0,0,"S")

mh0_ref_exp = g_mhsig0_ref_short.Eval(5.0,0,"S")
mh0_opt_exp = g_mhsig0_optimized_long.Eval(5.0,0,"S")

res_ref_exp = g_res_ref.Eval(10.0,0,"S")
res_opt_exp = g_res_opt.Eval(10.0,0,"S")

res_ref_at5sneg = res_ref90neg.Eval(cpvmax5s_ref_exp,0,"S")
res_opt_at5sneg = res_opt90neg.Eval(cpvmax5s_opt_exp,0,"S")

res_ref_at5spos = res_ref90.Eval(cpvmaxpos5s_ref_exp,0,"S")
res_opt_at5spos = res_opt90.Eval(cpvmaxpos5s_opt_exp,0,"S")

th23_ref_exp = g_resth23_ref.Eval(0.018,0,"S")
th23_opt_exp = g_resth23_opt.Eval(0.018,0,"S")

th13_ref_exp = g_resth13_ref.Eval(0.005,0,"S")
th13_opt_exp = g_resth13_opt.Eval(0.005,0,"S")

th13_004_ref_exp = g_resth13_ref.Eval(0.004,0,"S")
th13_004_opt_exp = g_resth13_opt.Eval(0.004,0,"S")

th13_003_ref_exp = g_resth13_ref.Eval(0.003,0,"S")
th13_003_opt_exp = g_resth13_opt.Eval(0.003,0,"S")


print "CPV 75%: ", cpv75_ref_exp, cpv75_opt_exp
print "CPV 50%: ", cpv50_ref_exp, cpv50_opt_exp
print "CPV -pi/2 3 sigma: ", cpvmax_ref_exp, cpvmax_opt_exp
print "CPV pi/2 3 sigma: ", cpvmaxpos_ref_exp, cpvmaxpos_opt_exp
print "CPV -pi/2 5 sigma: ", cpvmax5s_ref_exp, cpvmax5s_opt_exp
print "dcp resolution at -pi/2 discovery exposure: ", res_ref_at5sneg, res_opt_at5sneg
print "CPV pi/2 5 sigma: ", cpvmaxpos5s_ref_exp, cpvmaxpos5s_opt_exp
print "dcp resolution at pi/2 discovery exposure: ", res_ref_at5spos, res_opt_at5spos
print "MH 100%: ", mh_ref_exp, mh_opt_exp
print "MH 50%: ", mh50_ref_exp, mh50_opt_exp
print "MH 0%: ", mh0_ref_exp, mh0_opt_exp
print "Res 10 degs: ", res_ref_exp, res_opt_exp
print "q23 res 1 degs: ", th23_ref_exp, th23_opt_exp
print "sin22th13 res 0.005: ", th13_ref_exp, th13_opt_exp
print "sin22th13 res 0.004: ", th13_004_ref_exp, th13_004_opt_exp
print "sin22th13 res 0.003: ", th13_003_ref_exp, th13_003_opt_exp
