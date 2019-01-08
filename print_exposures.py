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

hier = sys.argv[1]
if (hier == 'no'):
      htext = "Normal Ordering"
elif (hier == 'io'):
      htext = "Inverted Ordering"
else:
      print "Must supply no or io!"
      exit()

explist = [0,1,5,10,28,50,100,200,300,400,556,600,800,984,1000,1250,1500]

cpvlist75_lo = [0]
cpvlist50_lo = [0]
cpvlistbest_lo = [0]
mhlist_lo = [0]
mhlistbest_lo = [0]

cpvlist75_hi = [0]
cpvlist50_hi = [0]
cpvlistbest_hi = [0]
mhlist_hi = [0]
mhlistbest_hi = [0]

cpvlist75_nom = [0]
cpvlist50_nom = [0]
cpvlistbest_nom = [0]
mhlist_nom = [0]
mhlistbest_nom = [0]

for myexp in explist:

      if (myexp==0):
            continue

      #q23lo (90% lower value)
      filename = "root/sens_optimized_long_q23lo_"+hier+"_exp"+str(myexp)+".root"
      f1 = ROOT.TFile(filename)
      cpvgraph_lo = f1.Get("CPVSig")
      mhgraph_lo = f1.Get("MHSig")
      nvals = cpvgraph_lo.GetN()
      cpv_vals = [ROOT.Double(0.0)]*nvals
      cpv_vals = array('d',cpv_vals)
      cpv_vals = cpvgraph_lo.GetY()

      mh_vals = [ROOT.Double(0.0)]*nvals
      mh_vals = array('d',mh_vals)
      mh_vals = mhgraph_lo.GetY()

      i = 0
      cpv_vals_lo = []
      mh_vals_lo = []
      while i < nvals:
            cpv_vals_lo.append(cpv_vals[i])
            mh_vals_lo.append(mh_vals[i])
            i += 1

      cpvsig_75_lo = sorted(cpv_vals_lo)[24]
      cpvsig_50_lo = sorted(cpv_vals_lo)[49]
      mhsig_100_lo = min(mh_vals_lo)
      cpvlist75_lo.append(cpvsig_75_lo)
      cpvlist50_lo.append(cpvsig_50_lo)
      cpvlistbest_lo.append(cpv_vals[26])
      mhlist_lo.append(mhsig_100_lo)
      mhlistbest_lo.append(mh_vals[26])
      f1.Close()

      #q23hi (90% upper value)
      filename = "root/sens_optimized_long_q23hi_"+hier+"_exp"+str(myexp)+".root"
      f1 = ROOT.TFile(filename)
      cpvgraph_hi = f1.Get("CPVSig")
      mhgraph_hi = f1.Get("MHSig")
      nvals = cpvgraph_hi.GetN()
      cpv_vals = [ROOT.Double(0.0)]*nvals
      cpv_vals = array('d',cpv_vals)
      cpv_vals = cpvgraph_hi.GetY()

      mh_vals = [ROOT.Double(0.0)]*nvals
      mh_vals = array('d',mh_vals)
      mh_vals = mhgraph_hi.GetY()

      i = 0
      cpv_vals_hi = []
      mh_vals_hi = []
      while i < nvals:
            cpv_vals_hi.append(cpv_vals[i])
            mh_vals_hi.append(mh_vals[i])
            i += 1

      cpvsig_75_hi = sorted(cpv_vals_hi)[24]
      cpvsig_50_hi = sorted(cpv_vals_hi)[49]
      mhsig_100_hi = min(mh_vals_hi)
      cpvlist75_hi.append(cpvsig_75_hi)
      cpvlist50_hi.append(cpvsig_50_hi)
      cpvlistbest_hi.append(cpv_vals[26])
      mhlist_hi.append(mhsig_100_hi)
      mhlistbest_hi.append(mh_vals[26])
      f1.Close()
      
      #Nominal q23 value

      filename = "root/sens_optimized_long_"+hier+"_exp"+str(myexp)+".root"
      f1 = ROOT.TFile(filename)
      cpvgraph_nom = f1.Get("CPVSig")
      mhgraph_nom = f1.Get("MHSig")
      nvals = cpvgraph_nom.GetN()
      cpv_vals = [ROOT.Double(0.0)]*nvals
      cpv_vals = array('d',cpv_vals)
      cpv_vals = cpvgraph_nom.GetY()

      mh_vals = [ROOT.Double(0.0)]*nvals
      mh_vals = array('d',mh_vals)
      mh_vals = mhgraph_nom.GetY()

      i = 0
      cpv_vals_nom = []
      mh_vals_nom = []
      while i < nvals:
            cpv_vals_nom.append(cpv_vals[i])
            mh_vals_nom.append(mh_vals[i])
            i += 1

      cpvsig_75_nom = sorted(cpv_vals_nom)[24]
      cpvsig_50_nom = sorted(cpv_vals_nom)[49]
      mhsig_100_nom = min(mh_vals_nom)
      cpvlist75_nom.append(cpvsig_75_nom)
      cpvlist50_nom.append(cpvsig_50_nom)
      cpvlistbest_nom.append(cpv_vals[26])
      mhlist_nom.append(mhsig_100_nom)
      mhlistbest_nom.append(mh_vals[26])
      f1.Close()
      

n = len(explist)
explist = array('d',explist)

cpvlist75_lo = array('d',cpvlist75_lo)
cpvlist50_lo = array('d',cpvlist50_lo)
cpvlistbest_lo = array('d',cpvlistbest_lo)
mhlist_lo = array('d',mhlist_lo)
mhlistbest_lo = array('d',mhlistbest_lo)

cpvlist75_hi = array('d',cpvlist75_hi)
cpvlist50_hi = array('d',cpvlist50_hi)
cpvlistbest_hi = array('d',cpvlistbest_hi)
mhlist_hi = array('d',mhlist_hi)
mhlistbest_hi = array('d',mhlistbest_hi)

cpvlist75_nom = array('d',cpvlist75_nom)
cpvlist50_nom = array('d',cpvlist50_nom)
cpvlistbest_nom = array('d',cpvlistbest_nom)
mhlist_nom = array('d',mhlist_nom)
mhlistbest_nom = array('d',mhlistbest_nom)

g_cpvsig_75_lo = ROOT.TGraph(n,explist,cpvlist75_lo)
g_cpvsig_50_lo = ROOT.TGraph(n,explist,cpvlist50_lo)
g_cpvsig_best_lo = ROOT.TGraph(n,explist,cpvlistbest_lo)
g_mhsig_lo = ROOT.TGraph(n,explist,mhlist_lo)
g_mhsig_best_lo = ROOT.TGraph(n,explist,mhlistbest_lo)

g_cpvsig_75_hi = ROOT.TGraph(n,explist,cpvlist75_hi)
g_cpvsig_50_hi = ROOT.TGraph(n,explist,cpvlist50_hi)
g_cpvsig_best_hi = ROOT.TGraph(n,explist,cpvlistbest_hi)
g_mhsig_hi = ROOT.TGraph(n,explist,mhlist_hi)
g_mhsig_best_hi = ROOT.TGraph(n,explist,mhlistbest_hi)

g_cpvsig_75_nom = ROOT.TGraph(n,explist,cpvlist75_nom)
g_cpvsig_50_nom = ROOT.TGraph(n,explist,cpvlist50_nom)
g_cpvsig_best_nom = ROOT.TGraph(n,explist,cpvlistbest_nom)
g_mhsig_nom = ROOT.TGraph(n,explist,mhlist_nom)
g_mhsig_best_nom = ROOT.TGraph(n,explist,mhlistbest_nom)


f2 = ROOT.TFile("root/resdcp0_optimized_long_no.root")
res_opt = f2.Get("Res")
nres = res_opt.GetN()
myexpvals = [ROOT.Double(0.0)]*nvals
mycpvvals = [ROOT.Double(0.0)]*nvals
myexpvals = array('d',myexpvals)
mycpvvals = array('d',mycpvvals)
myexpvals = res_opt.GetX()
mycpvvals = res_opt.GetY()
g_res_opt = ROOT.TGraph(nres,mycpvvals,myexpvals)

f4 = ROOT.TFile("root/resdcp90_optimized_long_no.root")
res_opt90 = f4.Get("Res")

f6 = ROOT.TFile("root/resdcp-90_optimized_long_no.root")
res_opt90neg = f6.Get("Res")

f8 = ROOT.TFile("root/resth23_optimized_long_no.root")
resth23_opt = f8.Get("Res")
nres = resth23_opt.GetN()
myexpvals = [ROOT.Double(0.0)]*nvals
mycpvvals = [ROOT.Double(0.0)]*nvals
myexpvals = array('d',myexpvals)
mycpvvals = array('d',mycpvvals)
myexpvals = resth23_opt.GetX()
mycpvvals = resth23_opt.GetY()
g_resth23_opt = ROOT.TGraph(nres,mycpvvals,myexpvals)

f10 = ROOT.TFile("root/resth13_optimized_long_no.root")
resth13_opt = f10.Get("Res")
nres = resth13_opt.GetN()
myexpvals = [ROOT.Double(0.0)]*nvals
mycpvvals = [ROOT.Double(0.0)]*nvals
myexpvals = array('d',myexpvals)
mycpvvals = array('d',mycpvvals)
myexpvals = resth13_opt.GetX()
mycpvvals = resth13_opt.GetY()
g_resth13_opt = ROOT.TGraph(nres,mycpvvals,myexpvals)

f11 = ROOT.TFile("root/staging_convert.root")
g_exp = f11.Get("g_exp")

#Fill exposure graphs backwards
g_cpvsig_75_optimized_long = ROOT.TGraph(n,cpvlist75_nom,explist)

g_cpvsig_50_optimized_long = ROOT.TGraph(n,cpvlist50_nom,explist)

g_mhsig_optimized_long = ROOT.TGraph(n,mhlist_nom,explist)

g_mhsig0_optimized_long = ROOT.TGraph(n,mhlistbest_nom,explist)

g_cpvmax_optimized_long = ROOT.TGraph(n,cpvlistbest_nom,explist)


#Get numbers I want

cpv75_opt_exp = g_cpvsig_75_optimized_long.Eval(3.0,0,"S")

cpv50_opt_exp = g_cpvsig_50_optimized_long.Eval(5.0,0,"S")

cpvmax_opt_exp = g_cpvmax_optimized_long.Eval(3.0,0,"S")

cpvmax5s_opt_exp = g_cpvmax_optimized_long.Eval(5.0,0,"S")

mh_opt_exp = g_mhsig_optimized_long.Eval(5.0,0,"S")

mh0_opt_exp = g_mhsig0_optimized_long.Eval(5.0,0,"S")

res_opt_exp = g_res_opt.Eval(10.0,0,"S")

res_opt_at5sneg = res_opt90neg.Eval(cpvmax5s_opt_exp,0,"S")

th23_opt_exp = g_resth23_opt.Eval(0.018,0,"S")

th13_opt_exp = g_resth13_opt.Eval(0.005,0,"S")

th13_004_opt_exp = g_resth13_opt.Eval(0.004,0,"S")

th13_003_opt_exp = g_resth13_opt.Eval(0.003,0,"S")


print "CPV 75% (3 sigma): ", cpv75_opt_exp, g_exp.Eval(cpv75_opt_exp,0,"S")
print "CPV 50% (5 sigma): ", cpv50_opt_exp, g_exp.Eval(cpv50_opt_exp,0,"S")
print "CPV -pi/2 3 sigma: ", cpvmax_opt_exp, g_exp.Eval(cpvmax_opt_exp,0,"S")
print "CPV -pi/2 5 sigma: ", cpvmax5s_opt_exp, g_exp.Eval(cpvmax5s_opt_exp,0,"S")
print "dcp resolution at -pi/2 discovery exposure: ", res_opt_at5sneg, g_exp.Eval(res_opt_at5sneg,0,"S")
print "MH 100%: ", mh_opt_exp, g_exp.Eval(mh_opt_exp,0,"S")
print "MH 0%: ", mh0_opt_exp, g_exp.Eval(mh0_opt_exp,0,"S")
print "Res 10 degs: ", res_opt_exp, g_exp.Eval(res_opt_exp,0,"S")
print "q23 res 1 degs: ", th23_opt_exp, g_exp.Eval(th23_opt_exp,0,"S")
print "sin22th13 res 0.005: ", th13_opt_exp, g_exp.Eval(th13_opt_exp,0,"S")
print "sin22th13 res 0.004: ", th13_004_opt_exp, g_exp.Eval(th13_004_opt_exp,0,"S")
print "sin22th13 res 0.003: ", th13_003_opt_exp, g_exp.Eval(th13_003_opt_exp,0,"S")

