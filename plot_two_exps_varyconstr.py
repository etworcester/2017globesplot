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

f2text = "root/sens_optimized_long_"+hier+"_noconstr_exp300.root"
f2 = ROOT.TFile(f2text)
cpv2 = f2.Get("CPVSig")
mh2 = f2.Get("MHSig")

f3text = "root/sens_optimized_long_"+hier+"_exp556.root"
f3 = ROOT.TFile(f3text)
cpv3 = f3.Get("CPVSig")
mh3 = f3.Get("MHSig")

f4text = "root/sens_optimized_long_"+hier+"_noconstr_exp556.root"
f4 = ROOT.TFile(f4text)
cpv4 = f4.Get("CPVSig")
mh4 = f4.Get("MHSig")

graph_cpvrange1 = filldiff(cpv1,cpv2)
graph_mhrange1 = filldiff(mh1,mh2)

graph_cpvrange2 = filldiff(cpv3,cpv4)
graph_mhrange2 = filldiff(mh3,mh4)

cpv2.SetLineWidth(3)
cpv1.SetLineWidth(3)
cpv2.SetLineStyle(2)

mh2.SetLineWidth(3)
mh1.SetLineWidth(3)
mh2.SetLineStyle(2)

cpv4.SetLineWidth(3)
cpv3.SetLineWidth(3)
cpv4.SetLineStyle(2)

mh4.SetLineWidth(3)
mh3.SetLineWidth(3)
mh4.SetLineStyle(2)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
#c1.SetGridx(1)
#c1.SetGridy(1)
h1 = c1.DrawFrame(-1.0,0.0,1.0,10.0)
h1.SetTitle("CP Violation Sensitivity")
h1.GetXaxis().SetTitle("#delta_{CP}/#pi")
h1.GetXaxis().CenterTitle()
h1.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h1.GetYaxis().SetTitleOffset(1.3)
h1.GetYaxis().CenterTitle()
c1.Modified()
graph_cpvrange1.SetFillColor(ROOT.kGreen-7)
graph_cpvrange1.Draw("F same")
graph_cpvrange2.SetFillColor(ROOT.kOrange-3)
graph_cpvrange2.Draw("F same")
#graph_cpvrange3.SetFillColor(ROOT.kBlue-7)
#graph_cpvrange3.Draw("F same")
cpv2.Draw("L same")
cpv1.Draw("L same")
cpv4.Draw("L same")
cpv3.Draw("L same")
ROOT.gPad.RedrawAxis()

t1 = ROOT.TPaveText(0.16,0.75,0.45,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText(htext)
t1.AddText("sin^{2}2#theta_{13} = 0.085 #pm 0.003")
if (hier == 'no'):
      t1.AddText("sin^{2}#theta_{23} = 0.441 #pm 0.042")
elif (hier == 'io'):
      t1.AddText("sin^{2}#theta_{23} = 0.587 #pm 0.042")
t1.SetFillColor(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.5,0.72,0.89,0.89)
l1.AddEntry(graph_cpvrange1,"7 years (staged)", "F")
l1.AddEntry(graph_cpvrange2,"10 years (staged)", "F")
l1.AddEntry(cpv1,"Nominal analysis","L")
l1.AddEntry(cpv2,"#theta_{13} & #theta_{23} unconstrained","L")
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
outname = "plots/cpv_two_exps_varyconstr_"+hier+"_2017.eps"
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
graph_mhrange1.Draw("F same")
graph_mhrange2.SetFillColor(ROOT.kOrange-3)
graph_mhrange2.Draw("F same")
mh2.Draw("L same")
mh1.Draw("L same")
mh4.Draw("L same")
mh3.Draw("L same")
ROOT.gPad.RedrawAxis()

l1.Draw("same")
t1.Draw("same")
line2.Draw("same")

outname = "plots/mh_two_exps_varyconstr_"+hier+"_2017.eps"
c2.SaveAs(outname)
