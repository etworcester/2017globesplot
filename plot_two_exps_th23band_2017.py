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

f1text = "root/sens_optimized_long_"+hier+"_exp300.root"
f1 = ROOT.TFile(f1text)
cpv1 = f1.Get("CPVSig")
mh1 = f1.Get("MHSig")

f1lotext = "root/sens_optimized_long_q23lo_"+hier+"_exp300.root"
f1lo = ROOT.TFile(f1lotext)
cpv1lo = f1lo.Get("CPVSig")
mh1lo = f1lo.Get("MHSig")

f1hitext = "root/sens_optimized_long_q23hi_"+hier+"_exp300.root"
f1hi = ROOT.TFile(f1hitext)
cpv1hi = f1hi.Get("CPVSig")
mh1hi = f1hi.Get("MHSig")

f3text = "root/sens_optimized_long_"+hier+"_exp556.root"
f3 = ROOT.TFile(f3text)
cpv3 = f3.Get("CPVSig")
mh3 = f3.Get("MHSig")

f3lotext = "root/sens_optimized_long_q23lo_"+hier+"_exp556.root"
f3lo = ROOT.TFile(f3lotext)
cpv3lo = f3lo.Get("CPVSig")
mh3lo = f3lo.Get("MHSig")

f3hitext = "root/sens_optimized_long_q23hi_"+hier+"_exp556.root"
f3hi = ROOT.TFile(f3hitext)
cpv3hi = f3hi.Get("CPVSig")
mh3hi = f3hi.Get("MHSig")

graph_cpvrange1 = filldiff(cpv1lo,cpv1hi)
graph_mhrange1 = filldiff(mh1hi,mh1lo)

graph_cpvrange3 = filldiff(cpv3lo,cpv3hi)
graph_mhrange3 = filldiff(mh3hi,mh3lo)

cpv1.SetLineWidth(3)
mh1.SetLineWidth(3)
cpv1.SetLineStyle(2)
mh1.SetLineStyle(2)

cpv3.SetLineWidth(3)
mh3.SetLineWidth(3)
cpv3.SetLineStyle(2)
mh3.SetLineStyle(2)

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
graph_cpvrange1.SetFillColor(ROOT.kGreen-7)
graph_cpvrange1.SetLineWidth(0)
graph_cpvrange1.Draw("F same")
graph_cpvrange3.SetFillColor(ROOT.kOrange-3)
graph_cpvrange3.SetLineWidth(0)
graph_cpvrange3.Draw("F same")
cpv1.Draw("L same")
cpv3.Draw("L same")
ROOT.gPad.RedrawAxis()

t1 = ROOT.TPaveText(0.16,0.75,0.53,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText(htext)
t1.AddText("sin^{2}2#theta_{13} = 0.085 #pm 0.003")
t1.AddText("#theta_{23}: NuFit 2016 (90% C.L. range)")
t1.SetFillColor(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.55,0.75,0.89,0.89)
l1.AddEntry(graph_cpvrange1,"7 years (staged)", "F")
l1.AddEntry(graph_cpvrange3,"10 years (staged)", "F")
if (hier == 'no'):
      l1.AddEntry(cpv1,"sin^{2}#theta_{23} = 0.441 #pm 0.042", "L")
elif (hier == 'io'):
      l1.AddEntry(cpv1,"sin^{2}#theta_{23} = 0.587 #pm 0.042", "L")      
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
outname = "plots/cpv_two_exps_th23band_"+hier+"_2017.eps"
c1.SaveAs(outname)

c2 = ROOT.TCanvas("c2","c2",800,800)
c2.SetLeftMargin(0.15)
h2 = c2.DrawFrame(-1.0,0.0,1.0,30.0)
h2.SetTitle("Mass Hierarchy Sensitivity")
h2.GetXaxis().SetTitle("#delta_{CP}/#pi")
h2.GetXaxis().CenterTitle()
h2.GetYaxis().SetTitle("#sqrt{#bar{#Delta#chi^{2}}}")
h2.GetYaxis().CenterTitle()
h2.GetYaxis().SetTitleOffset(1.3)
c2.Modified()
graph_mhrange1.SetFillColor(ROOT.kGreen-7)
graph_mhrange1.SetLineWidth(0)
graph_mhrange1.Draw("F same")
graph_mhrange3.SetFillColor(ROOT.kOrange-3)
graph_mhrange3.SetLineWidth(0)
graph_mhrange3.Draw("F same")
mh1.Draw("L same")
mh3.Draw("L same")
ROOT.gPad.RedrawAxis()

l1.Draw("same")
t1.Draw("same")
line2.Draw("same")

outname = "plots/mh_two_exps_th23band_"+hier+"_2017.eps"
c2.SaveAs(outname)

