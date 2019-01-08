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

explist = [1,5,10,28,50,100,200,300,400,556,600,800,984,1000,1250,1500]

cpvlist50_optimized_long = []
cpvlist75_optimized_long = []
cpvlistbest_optimized_long = []
mhlist_optimized_long = []
mhlist_best_optimized_long = []
cpvlist50_optimized_long_1pc = []
cpvlist75_optimized_long_1pc = []
cpvlistbest_optimized_long_1pc = []
mhlist_optimized_long_1pc = []
mhlist_best_optimized_long_1pc = []
cpvlist50_optimized_long_3pc = []
cpvlist75_optimized_long_3pc = []
cpvlistbest_optimized_long_3pc = []
mhlist_optimized_long_3pc = []
mhlist_best_optimized_long_3pc = []

for myexp in explist:
      
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
      cpvsig_best_optimized_long = cpv_vals_optimized_long[26]
      mhsig_100_optimized_long = min(mh_vals_optimized_long)
      mhsig_best_optimized_long = mh_vals[26]
      cpvlist75_optimized_long.append(cpvsig_75_optimized_long)
      cpvlist50_optimized_long.append(cpvsig_50_optimized_long)
      cpvlistbest_optimized_long.append(cpvsig_best_optimized_long)
      mhlist_optimized_long.append(mhsig_100_optimized_long)
      mhlist_best_optimized_long.append(mhsig_best_optimized_long)
      f1.Close()

      filename = "root/sens_optimized_long_syst1pc_no_exp"+str(myexp)+".root"
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

      cpvsig_75_optimized_long_1pc = sorted(cpv_vals_optimized_long)[24]
      cpvsig_50_optimized_long_1pc = sorted(cpv_vals_optimized_long)[49]
      cpvsig_best_optimized_long_1pc = cpv_vals_optimized_long[26]
      mhsig_100_optimized_long_1pc = min(mh_vals_optimized_long)
      mhsig_best_optimized_long_1pc = mh_vals[26]
      cpvlist75_optimized_long_1pc.append(cpvsig_75_optimized_long_1pc)
      cpvlist50_optimized_long_1pc.append(cpvsig_50_optimized_long_1pc)
      cpvlistbest_optimized_long_1pc.append(cpvsig_best_optimized_long_1pc)
      mhlist_optimized_long_1pc.append(mhsig_100_optimized_long_1pc)
      mhlist_best_optimized_long_1pc.append(mhsig_best_optimized_long_1pc)
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
      cpvsig_best_optimized_long_3pc = cpv_vals_optimized_long[26]
      mhsig_100_optimized_long_3pc = min(mh_vals_optimized_long)
      mhsig_best_optimized_long_3pc = mh_vals[26]
      cpvlist75_optimized_long_3pc.append(cpvsig_75_optimized_long_3pc)
      cpvlist50_optimized_long_3pc.append(cpvsig_50_optimized_long_3pc)
      cpvlistbest_optimized_long_3pc.append(cpvsig_best_optimized_long_3pc)
      mhlist_optimized_long_3pc.append(mhsig_100_optimized_long_3pc)
      mhlist_best_optimized_long_3pc.append(mhsig_best_optimized_long_3pc)
      f1.Close()
            

n = len(explist)
explist = array('d',explist)
cpvlist75_optimized_long = array('d',cpvlist75_optimized_long)
cpvlist75_optimized_long_1pc = array('d',cpvlist75_optimized_long_1pc)
cpvlist75_optimized_long_3pc = array('d',cpvlist75_optimized_long_3pc)

cpvlist50_optimized_long = array('d',cpvlist50_optimized_long)
cpvlist50_optimized_long_1pc = array('d',cpvlist50_optimized_long_1pc)
cpvlist50_optimized_long_3pc = array('d',cpvlist50_optimized_long_3pc)

cpvlistbest_optimized_long = array('d',cpvlistbest_optimized_long)
cpvlistbest_optimized_long_1pc = array('d',cpvlistbest_optimized_long_1pc)
cpvlistbest_optimized_long_3pc = array('d',cpvlistbest_optimized_long_3pc)

mhlist_optimized_long = array('d',mhlist_optimized_long)
mhlist_optimized_long_1pc = array('d',mhlist_optimized_long_1pc)
mhlist_optimized_long_3pc = array('d',mhlist_optimized_long_3pc)

mhlist_best_optimized_long = array('d',mhlist_best_optimized_long)
mhlist_best_optimized_long_1pc = array('d',mhlist_best_optimized_long_1pc)
mhlist_best_optimized_long_3pc = array('d',mhlist_best_optimized_long_3pc)

g_cpvsig_75_optimized_long = ROOT.TGraph(n,explist,cpvlist75_optimized_long)
g_cpvsig_75_optimized_long_1pc = ROOT.TGraph(n,explist,cpvlist75_optimized_long_1pc)
g_cpvsig_75_optimized_long_3pc = ROOT.TGraph(n,explist,cpvlist75_optimized_long_3pc)

g_cpvsig_50_optimized_long = ROOT.TGraph(n,explist,cpvlist50_optimized_long)
g_cpvsig_50_optimized_long_1pc = ROOT.TGraph(n,explist,cpvlist50_optimized_long_1pc)
g_cpvsig_50_optimized_long_3pc = ROOT.TGraph(n,explist,cpvlist50_optimized_long_3pc)

g_cpvsig_best_optimized_long = ROOT.TGraph(n,explist,cpvlistbest_optimized_long)
g_cpvsig_best_optimized_long_1pc = ROOT.TGraph(n,explist,cpvlistbest_optimized_long_1pc)
g_cpvsig_best_optimized_long_3pc = ROOT.TGraph(n,explist,cpvlistbest_optimized_long_3pc)

g_mhsig_100_optimized_long = ROOT.TGraph(n,explist,mhlist_optimized_long)
g_mhsig_100_optimized_long_1pc = ROOT.TGraph(n,explist,mhlist_optimized_long_1pc)
g_mhsig_100_optimized_long_3pc = ROOT.TGraph(n,explist,mhlist_optimized_long_3pc)

g_mhsig_best_optimized_long = ROOT.TGraph(n,explist,mhlist_best_optimized_long)
g_mhsig_best_optimized_long_1pc = ROOT.TGraph(n,explist,mhlist_best_optimized_long_1pc)
g_mhsig_best_optimized_long_3pc = ROOT.TGraph(n,explist,mhlist_best_optimized_long_3pc)

g_cpvsig_75_optimized_long.SetLineWidth(3)
g_cpvsig_75_optimized_long_1pc.SetLineWidth(3)
g_cpvsig_75_optimized_long_1pc.SetLineStyle(2)
g_cpvsig_75_optimized_long_3pc.SetLineWidth(3)
g_cpvsig_75_optimized_long_3pc.SetLineStyle(3)

g_cpvsig_50_optimized_long.SetLineWidth(3)
g_cpvsig_50_optimized_long_1pc.SetLineWidth(3)
g_cpvsig_50_optimized_long_1pc.SetLineStyle(2)
g_cpvsig_50_optimized_long_3pc.SetLineWidth(3)
g_cpvsig_50_optimized_long_3pc.SetLineStyle(3)

g_cpvsig_best_optimized_long.SetLineWidth(3)
g_cpvsig_best_optimized_long_1pc.SetLineWidth(3)
g_cpvsig_best_optimized_long_1pc.SetLineStyle(2)
g_cpvsig_best_optimized_long_3pc.SetLineWidth(3)
g_cpvsig_best_optimized_long_3pc.SetLineStyle(3)

g_mhsig_100_optimized_long.SetLineWidth(3)
g_mhsig_100_optimized_long_1pc.SetLineWidth(3)
g_mhsig_100_optimized_long_1pc.SetLineStyle(2)
g_mhsig_100_optimized_long_3pc.SetLineWidth(3)
g_mhsig_100_optimized_long_3pc.SetLineStyle(3)

g_mhsig_best_optimized_long.SetLineWidth(3)
g_mhsig_best_optimized_long_1pc.SetLineWidth(3)
g_mhsig_best_optimized_long_1pc.SetLineStyle(2)
g_mhsig_best_optimized_long_3pc.SetLineWidth(3)
g_mhsig_best_optimized_long_3pc.SetLineStyle(3)

graph_cpvrange75_opt = filldiff(g_cpvsig_75_optimized_long_1pc,g_cpvsig_75_optimized_long_3pc)
graph_cpvrange50_opt = filldiff(g_cpvsig_50_optimized_long_1pc,g_cpvsig_50_optimized_long_3pc)
graph_cpvrangebest_opt = filldiff(g_cpvsig_best_optimized_long_1pc,g_cpvsig_best_optimized_long_3pc)
graph_mhrange_opt = filldiff(g_mhsig_100_optimized_long_1pc,g_mhsig_100_optimized_long_3pc)
graph_mhrangebest_opt = filldiff(g_mhsig_best_optimized_long_1pc,g_mhsig_best_optimized_long_3pc)


c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0,0.0,1500.0,15.0)
h1.SetTitle("CP Violation Sensitivity")
h1.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h1.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h1.GetYaxis().SetTitleOffset(1.3)
h1.GetYaxis().CenterTitle()
c1.SetGridx(1)
c1.SetGridy(1)
c1.Modified()
graph_cpvrange75_opt.SetFillColor(ROOT.kCyan+2)
graph_cpvrange75_opt.SetLineWidth(0)
graph_cpvrange75_opt.Draw("F same")
graph_cpvrange50_opt.SetFillColor(ROOT.kCyan-7)
graph_cpvrange50_opt.SetLineWidth(0)
graph_cpvrange50_opt.Draw("F same")
graph_cpvrangebest_opt.SetFillColor(ROOT.kPink-3)
graph_cpvrangebest_opt.SetLineWidth(0)
graph_cpvrangebest_opt.Draw("F same")
g_cpvsig_75_optimized_long_1pc.Draw("lsame")
g_cpvsig_75_optimized_long_3pc.Draw("lsame")
g_cpvsig_75_optimized_long.Draw("lsame")
g_cpvsig_50_optimized_long_1pc.Draw("lsame")
g_cpvsig_50_optimized_long_3pc.Draw("lsame")
g_cpvsig_50_optimized_long.Draw("lsame")
g_cpvsig_best_optimized_long_1pc.Draw("lsame")
g_cpvsig_best_optimized_long_3pc.Draw("lsame")
g_cpvsig_best_optimized_long.Draw("lsame")

t1 = ROOT.TPaveText(0.16,0.75,0.45,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("Normal Ordering")
t1.AddText("sin^{2}2#theta_{13} = 0.085 #pm 0.003")
t1.AddText("sin^{2}#theta_{23} = 0.441 #pm 0.042")
t1.SetFillColor(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.55,0.7,0.89,0.88)
l1.AddEntry(graph_cpvrangebest_opt, "#delta_{CP} = -#pi/2","F")
l1.AddEntry(graph_cpvrange50_opt, "50% of #delta_{CP} values","F")
l1.AddEntry(graph_cpvrange75_opt, "75% of #delta_{CP} values","F")
l1.AddEntry(g_cpvsig_75_optimized_long_1pc,"5% #oplus 1%","L")
l1.AddEntry(g_cpvsig_75_optimized_long,"Nominal: 5% #oplus 2%","L")
l1.AddEntry(g_cpvsig_75_optimized_long_3pc,"5% #oplus 3%","L")
l1.SetBorderSize(0)
l1.SetFillStyle(0)
l1.Draw("same")

line1 = ROOT.TLine(0.,3.,1500.,3.)
line1.SetLineStyle(2)
line1.SetLineWidth(3)
line1.Draw("same")

line2 = ROOT.TLine(0.0,5.,1500.,5.)
line2.SetLineStyle(2)
line2.SetLineWidth(3)
line2.Draw("same")

t3sig = ROOT.TPaveText(50.,3.1,100.,3.3)
t3sig.AddText("3#sigma")
t3sig.SetFillColor(0)
t3sig.SetBorderSize(0)
#t3sig.Draw("same")

t5sig = ROOT.TPaveText(50.,5.1,100.,5.3)
t5sig.AddText("5#sigma")
t5sig.SetFillColor(0)
t5sig.SetBorderSize(0)
#t5sig.Draw("same")

# t1pc = ROOT.TPaveText(1520.,3.3,1690,3.6)
# t1pc.AddText("5%#oplus1%")
# t1pc.SetFillColor(0)
# t1pc.SetBorderSize(0)
# t1pc.SetTextColor(ROOT.kBlue-1)
# t1pc.Draw("same")

# t2pc = ROOT.TPaveText(1520.,3.0,1690,3.3)
# t2pc.AddText("5%#oplus2%")
# t2pc.SetFillColor(0)
# t2pc.SetBorderSize(0)
# t2pc.SetTextColor(ROOT.kBlue-1)
# t2pc.Draw("same")

# t3pc = ROOT.TPaveText(1520.,2.65,1690,2.95)
# t3pc.AddText("5%#oplus3%")
# t3pc.SetFillColor(0)
# t3pc.SetBorderSize(0)
# t3pc.SetTextColor(ROOT.kBlue-1)
# t3pc.Draw("same")

outname = "plots/cpv_exp_syst_2017_test.png"
c1.SaveAs(outname)


c3 = ROOT.TCanvas("c3","c3",800,800)
c3.SetLeftMargin(0.15)
h3 = c3.DrawFrame(0,0.,500.0,13.0)
ROOT.gPad.SetTicks(0,1)
h3.SetTitle("MH Sensitivity")
h3.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h3.GetYaxis().SetTitle("#sqrt{#bar{#Delta#chi^{2}}}")
h3.GetYaxis().SetTitleOffset(1.3)
h3.GetYaxis().CenterTitle()
c3.Modified()
graph_mhrange_opt.SetFillColor(ROOT.kCyan+3)
graph_mhrange_opt.SetLineWidth(0)
graph_mhrangebest_opt.SetFillColor(ROOT.kPink-3)
graph_mhrangebest_opt.SetLineWidth(0)
graph_mhrange_opt.Draw("F same")
graph_mhrangebest_opt.Draw("F same")

g_mhsig_100_optimized_long.Draw("L same")
g_mhsig_100_optimized_long_1pc.Draw("L same")
g_mhsig_100_optimized_long_3pc.Draw("L same")
g_mhsig_best_optimized_long.Draw("L same")
g_mhsig_best_optimized_long_1pc.Draw("L same")
g_mhsig_best_optimized_long_3pc.Draw("L same")

lm1 = ROOT.TLegend(0.55,0.72,0.89,0.88)
lm1.AddEntry(graph_mhrangebest_opt, "#delta_{CP} = -#pi/2","F")
lm1.AddEntry(graph_mhrange_opt, "100% of #delta_{CP} values","F")
lm1.AddEntry(g_cpvsig_75_optimized_long_1pc,"5% #oplus 1%","L")
lm1.AddEntry(g_cpvsig_75_optimized_long,"Nominal: 5% #oplus 2%","L")
lm1.AddEntry(g_cpvsig_75_optimized_long_3pc,"5% #oplus 3%","L")
lm1.SetBorderSize(0)
lm1.SetFillStyle(0)
lm1.Draw("same")

t1.Draw("same")
line1.Draw("same")
line2.Draw("same")
#t3sig.Draw("same")
#t5sig.Draw("same")

# t1pc = ROOT.TPaveText(1520.,9.0,1690,9.5)
# t1pc.AddText("5%#oplus1%")
# t1pc.SetFillColor(0)
# t1pc.SetBorderSize(0)
# t1pc.SetTextColor(ROOT.kBlue-1)
# t1pc.Draw("same")

# t2pc = ROOT.TPaveText(1520.,8.5,1690,9.0)
# t2pc.AddText("5%#oplus2%")
# t2pc.SetFillColor(0)
# t2pc.SetBorderSize(0)
# t2pc.SetTextColor(ROOT.kBlue-1)
# t2pc.Draw("same")

# t3pc = ROOT.TPaveText(1520.,8.0,1690,8.5)
# t3pc.AddText("5%#oplus3%")
# t3pc.SetFillColor(0)
# t3pc.SetBorderSize(0)
# t3pc.SetTextColor(ROOT.kBlue-1)
# t3pc.Draw("same")

# t1pc_opt = ROOT.TPaveText(1520.,11.3,1690,11.8)
# t1pc_opt.AddText("5%#oplus1%")
# t1pc_opt.SetFillColor(0)
# t1pc_opt.SetBorderSize(0)
# t1pc_opt.SetTextColor(ROOT.kBlue-1)
# t1pc_opt.Draw("same")

# t2pc_opt = ROOT.TPaveText(1520.,10.8,1690,11.3)
# t2pc_opt.AddText("5%#oplus2%")
# t2pc_opt.SetFillColor(0)
# t2pc_opt.SetBorderSize(0)
# t2pc_opt.SetTextColor(ROOT.kBlue-1)
# t2pc_opt.Draw("same")

# t3pc_opt = ROOT.TPaveText(1520.,10.3,1690,10.8)
# t3pc_opt.AddText("5%#oplus3%")
# t3pc_opt.SetFillColor(0)
# t3pc_opt.SetBorderSize(0)
# t3pc_opt.SetTextColor(ROOT.kBlue-1)
# t3pc_opt.Draw("same")

outname = "plots/mh_exp_syst_2017.eps"
c3.SaveAs(outname)

