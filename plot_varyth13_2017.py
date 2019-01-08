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
  
f1 = ROOT.TFile("root/sens_optimized_long_no_exp300.root")
cpv1 = f1.Get("CPVSig")
mh1 = f1.Get("MHSig")

f3 = ROOT.TFile("root/sens_optimized_long_oscpar_q13lo_no_exp300.root")
cpv3 = f3.Get("CPVSig")
mh3 = f3.Get("MHSig")

f4 = ROOT.TFile("root/sens_optimized_long_oscpar_q13hi_no_exp300.root")
cpv4 = f4.Get("CPVSig")
mh4 = f4.Get("MHSig")

ff1 = ROOT.TFile("root/sens_optimized_long_no_exp556.root")
cpv11 = ff1.Get("CPVSig")
mh11 = ff1.Get("MHSig")

ff3 = ROOT.TFile("root/sens_optimized_long_oscpar_q13lo_no_exp556.root")
cpv13 = ff3.Get("CPVSig")
mh13 = ff3.Get("MHSig")

ff4 = ROOT.TFile("root/sens_optimized_long_oscpar_q13hi_no_exp556.root")
cpv14 = ff4.Get("CPVSig")
mh14 = ff4.Get("MHSig")

graph_cpvrange300 = filldiff(cpv4,cpv3)
graph_cpvrange556 = filldiff(cpv14,cpv13)

graph_mhrange300 = filldiff(mh4,mh3)
graph_mhrange556 = filldiff(mh14,mh13)



cpv1.SetLineWidth(3)
cpv3.SetLineWidth(3)
cpv4.SetLineWidth(3)

cpv11.SetLineWidth(3)
cpv13.SetLineWidth(3)
cpv14.SetLineWidth(3)

cpv1.SetLineStyle(1)
cpv3.SetLineStyle(3)
cpv4.SetLineStyle(4)

cpv11.SetLineStyle(1)
cpv13.SetLineStyle(3)
cpv14.SetLineStyle(4)

#cpv1.SetLineColor(ROOT.kCyan)
#cpv3.SetLineColor(ROOT.kCyan)
#cpv4.SetLineColor(ROOT.kCyan)

#cpv11.SetLineColor(ROOT.kCyan)
#cpv13.SetLineColor(ROOT.kCyan)
#cpv14.SetLineColor(ROOT.kCyan)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(-1.0,0.0,1.0,10.0)
h1.SetTitle("CP Violation Sensitivity")
h1.GetXaxis().SetTitle("#delta_{CP}/#pi")
h1.GetXaxis().CenterTitle()
h1.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h1.GetYaxis().SetTitleOffset(1.3)
h1.GetYaxis().CenterTitle()
c1.Modified()
graph_cpvrange300.SetFillColor(ROOT.kCyan-1)
graph_cpvrange556.SetFillColor(ROOT.kCyan+1)
graph_cpvrange300.SetLineWidth(0)
graph_cpvrange556.SetLineWidth(0)
graph_cpvrange300.Draw("F same")
graph_cpvrange556.Draw("F same")
cpv1.Draw("L same")
cpv3.Draw("L same")
cpv4.Draw("L same")
cpv11.Draw("L same")
cpv13.Draw("L same")
cpv14.Draw("L same")
ROOT.gPad.RedrawAxis()

t1 = ROOT.TPaveText(0.16,0.75,0.45,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("Normal Ordering")
t1.AddText("sin^{2}#theta_{23} = 0.441 #pm 0.042")
t1.SetFillColor(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.55,0.75,0.89,0.89)
l1.AddEntry(graph_cpvrange300,"7 years (staged)","F")
l1.AddEntry(graph_cpvrange556,"10 years (staged)","F")
l1.AddEntry(cpv3,"sin^{2}2#theta_{13} = 0.075","L")
l1.AddEntry(cpv1,"sin^{2}2#theta_{13} = 0.085","L")
l1.AddEntry(cpv4,"sin^{2}2#theta_{13} = 0.093","L")

l1.SetBorderSize(0)

line1 = ROOT.TLine(-1.0,3.,1.0,3.)
line1.SetLineStyle(2)
line1.SetLineWidth(3)
line1.Draw("same")

line2 = ROOT.TLine(-1.0,5.,1.0,5.)
line2.SetLineStyle(2)
line2.SetLineWidth(3)
line2.Draw("same")

t3sig = ROOT.TPaveText(-0.05,3.1,0.05,3.5)
t3sig.AddText("3#sigma")
t3sig.SetFillColor(0)
t3sig.SetBorderSize(0)
t3sig.Draw("same")

t5sig = ROOT.TPaveText(-0.05,5.1,0.05,5.5)
t5sig.AddText("5#sigma")
t5sig.SetFillColor(0)
t5sig.SetBorderSize(0)
t5sig.Draw("same")

l1.SetFillColor(0)
l1.Draw("same")
outname = "plots/cpv_varyth13_2017.eps"
c1.SaveAs(outname)

mh1.SetLineWidth(3)
mh3.SetLineWidth(3)
mh4.SetLineWidth(3)

mh11.SetLineWidth(3)
mh13.SetLineWidth(3)
mh14.SetLineWidth(3)

mh1.SetLineStyle(1)
mh3.SetLineStyle(3)
mh4.SetLineStyle(4)

mh11.SetLineStyle(1)
mh13.SetLineStyle(3)
mh14.SetLineStyle(4)

c2 = ROOT.TCanvas("c2","c2",800,800)
c2.SetLeftMargin(0.15)
h2 = c2.DrawFrame(-1.0,0.0,1.0,30.0)
h2.SetTitle("Mass Hierarchy Sensitivity")
h2.GetXaxis().SetTitle("#delta_{CP}/#pi")
h2.GetXaxis().CenterTitle()
h2.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h2.GetYaxis().SetTitleOffset(1.3)
h2.GetYaxis().CenterTitle()
c2.Modified()
graph_mhrange300.SetFillColor(ROOT.kCyan-1)
graph_mhrange556.SetFillColor(ROOT.kCyan+1)
graph_mhrange300.SetLineWidth(0)
graph_mhrange556.SetLineWidth(0)
graph_mhrange300.Draw("F same")
graph_mhrange556.Draw("F same")
mh1.Draw("L same")
mh3.Draw("L same")
mh4.Draw("L same")
mh11.Draw("L same")
mh13.Draw("L same")
mh14.Draw("L same")
ROOT.gPad.RedrawAxis()

t1.Draw("same")

line2.Draw("same")

l1.Draw("same")

outname = "plots/mh_varyth13_2017.eps"
c2.SaveAs(outname)

