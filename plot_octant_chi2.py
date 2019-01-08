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


inopt = ROOT.TFile("root/sens_octant_optimized_long_no_exp300.root")
inopt556 = ROOT.TFile("root/sens_octant_optimized_long_no_exp556.root")

chi2_opt = inopt.Get("chi2_10to90")
chi2_opt556 = inopt556.Get("chi2_10to90")

xvals = []
yvals = []
xvals_556 = []
yvals_556 = []
np = chi2_opt.GetN()
np556 = chi2_opt556.GetN()

i = 0
x = ROOT.Double(0.0)
y = ROOT.Double(0.0)
x556 = ROOT.Double(0.0)
y556 = ROOT.Double(0.0)
while i < np:
    chi2_opt.GetPoint(i,x,y)
    if (int(10*x)==402):
        np = np-1
        i += 1
        print "skipping"
        continue
    xrad = x*math.pi/180
    xval = math.sin(xrad)*math.sin(xrad)
    xvals.append(float(xval))
    if (float(y)>0.00001):
        yval = math.sqrt(float(y))
    else:
        yval = 0.0
    yvals.append(yval)
    i += 1

i = 0
while i < np556:
    chi2_opt556.GetPoint(i,x556,y556)
    xrad556 = x556*math.pi/180
    xval556 = math.sin(xrad556)*math.sin(xrad556)    
    xvals_556.append(float(xval556))
    if (float(y556)>0.00001):
        yval556 = math.sqrt(float(y556))
    else:
        yval556 = 0.0
    yvals_556.append(yval556)
    i += 1

xvals = array('d',xvals)
yvals = array('d',yvals)
xvals_556 = array('d',xvals_556)
yvals_556 = array('d',yvals_556)

g_sin = ROOT.TGraph(np,xvals,yvals)
g_sin556 = ROOT.TGraph(np556,xvals_556,yvals_556)


c3 = ROOT.TCanvas("c3","c3",800,800)
h3 = c3.DrawFrame(0.328, 0.0, 0.671, 8.0)
h3.SetTitle("Octant Sensitivity")
h3.GetXaxis().SetTitle("sin^{2}#theta_{23}")
#h3.GetYaxis().SetTitleOffset(1.)
h3.GetXaxis().SetTitleOffset(1.15)
h3.GetYaxis().CenterTitle()
h3.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")

lo = math.sin(0.408)*math.sin(0.408)
hi = math.sin(0.5)*math.sin(0.5)
b1 = ROOT.TBox(0.408,0.0,0.50,8.0)
b1.SetFillColor(ROOT.kYellow-4)
b1.Draw("same")

g_sin.SetFillColor(ROOT.kGreen-7)
g_sin.Draw("Fsame")
g_sin556.SetFillColor(ROOT.kOrange-3)
g_sin556.Draw("Fsame")

leg1 = ROOT.TLegend(0.6,0.75,0.89,0.89)
leg1.AddEntry(g_sin,"7 years (staged)","F")
leg1.AddEntry(g_sin556,"10 years (staged)","F")
leg1.AddEntry(b1,"NuFit 2016 (90% C.L.)","f")
leg1.SetFillColor(0)
leg1.SetBorderSize(0)
leg1.Draw()

t1 = ROOT.TPaveText(0.11,0.8,0.4,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("Normal Ordering")
t1.AddText("sin^{2}2#theta_{13} = 0.085 #pm 0.003")
t1.SetFillColor(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLine(0.328,3.,0.671,3.0)
l1.SetLineWidth(3)
l1.SetLineStyle(2)
l1.Draw()

l2 = ROOT.TLine(0.328,5.,0.671,5.0)
l2.SetLineWidth(3)
l2.SetLineStyle(2)
l2.Draw()

ROOT.gPad.RedrawAxis()

c3.SaveAs("plots/octant_no_2017.eps")



    
