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
ROOT.gStyle.SetTitleSize(0.04,"t")

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

#Delta CP plot

f1 = ROOT.TFile("root/resdcp0_optimized_long_no_noconstr.root")
res1 = f1.Get("Res")

f2 = ROOT.TFile("root/resdcp0_optimized_long_no.root")
res2 = f2.Get("Res")

f3 = ROOT.TFile("root/resdcp-90_optimized_long_no_noconstr.root")
res3 = f3.Get("Res")

f4 = ROOT.TFile("root/resdcp-90_optimized_long_no.root")
res4 = f4.Get("Res")

graph_dcp0range = filldiff(res1,res2)
graph_dcp90range = filldiff(res3,res4)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0,0.0,1500.0,40.0)
h1.SetTitle("#delta_{CP} Resolution")
h1.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h1.GetYaxis().SetTitle("#delta_{CP} Resolution (degrees)")
h1.GetYaxis().SetTitleOffset(1.3)
h1.GetYaxis().CenterTitle()
c1.Modified()
graph_dcp0range.SetFillColor(ROOT.kCyan+2)
graph_dcp90range.SetFillColor(ROOT.kPink-3)
graph_dcp0range.Draw("Fsame")
graph_dcp90range.Draw("Fsame")

t1 = ROOT.TPaveText(0.5,0.7,0.88,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("Normal Ordering")
t1.AddText("sin^{2}2#theta_{13} = 0.085 #pm 0.003")
t1.AddText("sin^{2}#theta_{23} = 0.441 #pm 0.042")
t1.SetFillColor(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.5,0.5,0.88,0.7)
l1.AddEntry(graph_dcp90range,"#delta_{CP} = -#pi/2","F")
l1.AddEntry(graph_dcp0range,"#delta_{CP} = 0","F")
l1.AddEntry(res2,"Nominal Analysis","L")
l1.AddEntry(res1,"#theta_{13} & #theta_{23} unconstrained","L")
l1.SetBorderSize(0)
l1.SetFillStyle(0)
l1.Draw("same")

res1.SetLineWidth(3)
res2.SetLineWidth(3)
res3.SetLineWidth(3)
res4.SetLineWidth(3)

res1.SetLineStyle(2)
res3.SetLineStyle(2)

res1.Draw("L same")
res2.Draw("L same")
res3.Draw("L same")
res4.Draw("L same")

tzero = ROOT.TPaveText(1000,3.0,1200,6.0)
tzero.AddText("#delta_{CP} = 0#circ")
tzero.SetFillStyle(0)
tzero.SetBorderSize(0)
#tzero.Draw("same")

t90 = ROOT.TPaveText(1000,10.0,1225,14.0)
t90.AddText("#delta_{CP} = 90#circ")
t90.SetFillStyle(0)
t90.SetBorderSize(0)
#t90.Draw("same")

outname = "plots/res_dcp_exp_varyconstr_2017.eps"
c1.SaveAs(outname)

#sin2(2q13) resolution

f1 = ROOT.TFile("root/resth13_optimized_long_no_noconstr.root")
res1 = f1.Get("Res")

f2 = ROOT.TFile("root/resth13_optimized_long_no.root")
res2 = f2.Get("Res")

res1.SetLineWidth(3)
res1.SetLineColor(ROOT.kCyan+2)
res2.SetLineWidth(3)
res2.SetLineColor(ROOT.kCyan+2)


graph_range = filldiff(res1,res2)

c2 = ROOT.TCanvas("c2","c2",800,800)
c2.SetLeftMargin(0.15)
h2 = c2.DrawFrame(0,0.0,1500.0,0.02)
h2.SetTitle("sin^{2}2#theta_{13} Resolution")
h2.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h2.GetYaxis().SetTitle("sin^{2}2#theta_{13} Resolution")
h2.GetYaxis().SetTitleOffset(1.8)
h2.GetYaxis().CenterTitle()
c2.Modified()
graph_range.SetFillColor(ROOT.kCyan+2)
graph_range.Draw("Fsame")

t1.Draw("same")
res1.Draw("lsame")
res2.Draw("lsame")

outname = "plots/res_th13_exp_varyconstr_2017.eps"
c2.SaveAs(outname)

#sin2(q23) resolution

f1 = ROOT.TFile("root/resth23_optimized_long_no_noconstr.root")
res1 = f1.Get("Res")

f2 = ROOT.TFile("root/resth23_optimized_long_no.root")
res2 = f2.Get("Res")

res1.SetLineWidth(3)
res1.SetLineColor(ROOT.kCyan+2)
res2.SetLineWidth(3)
res2.SetLineColor(ROOT.kCyan+2)

graph_range = filldiff(res1,res2)

c3 = ROOT.TCanvas("c3","c3",800,800)
c3.SetLeftMargin(0.15)
h3 = c3.DrawFrame(0,0.0,1500.0,0.04)
h3.SetTitle("sin^{2}#theta_{23} Resolution")
h3.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h3.GetYaxis().SetTitle("sin^{2}#theta_{23} Resolution")
h3.GetYaxis().SetTitleOffset(1.8)
h3.GetYaxis().CenterTitle()
c3.Modified()
graph_range.SetFillColor(ROOT.kCyan+2)
graph_range.Draw("Fsame")

t1.Draw("same")
res1.Draw("lsame")
res2.Draw("lsame")

outname = "plots/res_th23_exp_varyconstr_2017.eps"
c3.SaveAs(outname)

#dmsq resolution

f1 = ROOT.TFile("root/resdm_optimized_long_no_noconstr.root")
res1 = f1.Get("Res")

f2 = ROOT.TFile("root/resdm_optimized_long_no.root")
res2 = f2.Get("Res")

res1.SetLineWidth(3)
res1.SetLineColor(ROOT.kCyan+2)
res2.SetLineWidth(3)
res2.SetLineColor(ROOT.kCyan+2)

graph_range = filldiff(res1,res2)

c4 = ROOT.TCanvas("c4","c4",800,800)
c4.SetLeftMargin(0.15)
h4 = c4.DrawFrame(0,0.0,1500.0,3.0)
h4.SetTitle("#Deltam^{2}_{31} Resolution")
h4.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h4.GetYaxis().SetTitle("#Deltam^{2}_{31} Resolution (eV^{2} #times 10^{-5})")
h4.GetYaxis().SetTitleOffset(1.8)
h4.GetYaxis().CenterTitle()
c4.Modified()
graph_range.SetFillColor(ROOT.kCyan+2)
graph_range.Draw("Fsame")

t1.Draw("same")
res1.Draw("lsame")
res2.Draw("lsame")

outname = "plots/res_dm_exp_varyconstr_2017.eps"
c4.SaveAs(outname)

