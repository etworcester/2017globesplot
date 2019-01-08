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

def rotate(hist):

    newy = hist.GetXaxis().GetXbins()
    newy = array('d',newy)
    title = hist.GetTitle()
    ny = hist.GetNbinsX()
    nx = hist.GetNbinsY()
    xlo = hist.GetYaxis().GetBinLowEdge(1)
    xhi = hist.GetYaxis().GetBinLowEdge(nx) + hist.GetYaxis().GetBinWidth(nx)
    newh = ROOT.TH2D("newh","title",nx,xlo,xhi,ny,newy)
    newh.SetDirectory(0)

    j = 1
    while j < nx+1:
        i = 1
        while i < ny+1:
            val = hist.GetBinContent(hist.GetBin(i,j))
            newh.SetBinContent(newh.GetBin(j,i),val)
            #if j==1:
                #print i,j,hist.GetBin(i,j), newh.GetBin(j,i), val, newh.GetBinContent(newh.GetBin(j,i))
                #print i,j, hist.GetXaxis().GetBinCenter(i), newh.GetYaxis().GetBinCenter(i)
            i += 1
        j += 1
        
    return newh


f1 = ROOT.TFile("root/Bubbles_q23_exp300.root")
rc1_300 = f1.Get("Chi2Map_0")
rc2_300 = f1.Get("Chi2Map_1")
rc3_300 = f1.Get("Chi2Map_2")
rc4_300 = f1.Get("Chi2Map_3")
rc5_300 = f1.Get("Chi2Map_4")
rc6_300 = f1.Get("Chi2Map_5")
rc7_300 = f1.Get("Chi2Map_6")
rc8_300 = f1.Get("Chi2Map_7")
rc9_300 = f1.Get("Chi2Map_8")
rc10_300 = f1.Get("Chi2Map_9")
rc11_300 = f1.Get("Chi2Map_10")
rc12_300 = f1.Get("Chi2Map_11")

c1_300 = rotate(rc1_300)
c2_300 = rotate(rc2_300)
c3_300 = rotate(rc3_300)
c4_300 = rotate(rc4_300)
c5_300 = rotate(rc5_300)
c6_300 = rotate(rc6_300)
c7_300 = rotate(rc7_300)
c8_300 = rotate(rc8_300)
c9_300 = rotate(rc9_300)
c10_300= rotate(rc10_300)
c11_300= rotate(rc11_300)
c12_300= rotate(rc12_300)

list300 = [c1_300,c2_300,c3_300,c4_300,c5_300,c6_300,c7_300,c8_300,c9_300,c10_300,c11_300,c12_300]

f2 = ROOT.TFile("root/Bubbles_q23_exp556.root")
rc1_556 = f2.Get("Chi2Map_0")
rc2_556 = f2.Get("Chi2Map_1")
rc3_556 = f2.Get("Chi2Map_2")
rc4_556 = f2.Get("Chi2Map_3")
rc5_556 = f2.Get("Chi2Map_4")
rc6_556 = f2.Get("Chi2Map_5")
rc7_556 = f2.Get("Chi2Map_6")
rc8_556 = f2.Get("Chi2Map_7")
rc9_556 = f2.Get("Chi2Map_8")
rc10_556 = f2.Get("Chi2Map_9")
rc11_556 = f2.Get("Chi2Map_10")
rc12_556 = f2.Get("Chi2Map_11")

c1_556 = rotate(rc1_556)
c2_556 = rotate(rc2_556)
c3_556 = rotate(rc3_556)
c4_556 = rotate(rc4_556)
c5_556 = rotate(rc5_556)
c6_556 = rotate(rc6_556)
c7_556 = rotate(rc7_556)
c8_556 = rotate(rc8_556)
c9_556 = rotate(rc9_556)
c10_556= rotate(rc10_556)
c11_556= rotate(rc11_556)
c12_556= rotate(rc12_556)

list556 = [c1_556,c2_556,c3_556,c4_556,c5_556,c6_556,c7_556,c8_556,c9_556,c10_556,c11_556,c12_556]

f3 = ROOT.TFile("root/Bubbles_q23_exp984.root")
rc1_984 = f3.Get("Chi2Map_0")
rc2_984 = f3.Get("Chi2Map_1")
rc3_984 = f3.Get("Chi2Map_2")
rc4_984 = f3.Get("Chi2Map_3")
rc5_984 = f3.Get("Chi2Map_4")
rc6_984 = f3.Get("Chi2Map_5")
rc7_984 = f3.Get("Chi2Map_6")
rc8_984 = f3.Get("Chi2Map_7")
rc9_984 = f3.Get("Chi2Map_8")
rc10_984 = f3.Get("Chi2Map_9")
rc11_984 = f3.Get("Chi2Map_10")
rc12_984 = f3.Get("Chi2Map_11")

c1_984 = rotate(rc1_984)
c2_984 = rotate(rc2_984)
c3_984 = rotate(rc3_984)
c4_984 = rotate(rc4_984)
c5_984 = rotate(rc5_984)
c6_984 = rotate(rc6_984)
c7_984 = rotate(rc7_984)
c8_984 = rotate(rc8_984)
c9_984 = rotate(rc9_984)
c10_984= rotate(rc10_984)
c11_984= rotate(rc11_984)
c12_984= rotate(rc12_984)

list984 = [c1_984,c2_984,c3_984,c4_984,c5_984,c6_984,c7_984,c8_984,c9_984,c10_984,c11_984,c12_984]

nufit = ROOT.TFile("root/nufit_dcpvq23_contours_rotate.root")
h_no = nufit.Get("h_no")

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(-180,0.3,180,0.8)
h1.GetYaxis().SetTitle("sin^{2}#theta_{23}")
h1.GetXaxis().SetTitle("#delta_{CP} (degrees)")
h1.GetYaxis().SetTitleOffset(1.7)
c1.Modified()

#Not to plot, just for the legend
box1 = ROOT.TBox(41.1,-180,43.8,120)
box1.SetFillColor(ROOT.kYellow-7)
box1.SetLineWidth(0)

t1 = ROOT.TPaveText(0.16,0.75,0.5,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("Normal Ordering")
t1.AddText("sin^{2}2#theta_{13} = 0.085 #pm 0.003")
t1.AddText("90% C.L. (2 d.o.f.)")
t1.SetFillColor(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

h_no.Draw("cont0 same")
h_no.SetContour(2)
h_no.SetContourLevel(0,0)
h_no.SetContourLevel(1,4.61)
colors = [ROOT.kYellow-7]
colors = array('i',colors)
ROOT.gStyle.SetPalette(1,colors)

for plot in list300:
    plot.SetContour(1)
    plot.SetContourLevel(0,4.61)
    plot.SetLineWidth(3)
    plot.SetLineColor(ROOT.kGreen-7)
    plot.Draw("cont3 same")

for plot in list556:
    plot.SetContour(1)
    plot.SetContourLevel(0,4.61)
    plot.SetLineWidth(3)
    plot.SetLineColor(ROOT.kOrange-3)
    plot.Draw("cont3 same")

for plot in list984:
    plot.SetContour(1)
    plot.SetContourLevel(0,4.61)
    plot.SetLineWidth(3)
    plot.SetLineColor(ROOT.kBlue-7)
    plot.Draw("cont3 same")

#must be fixed - just a placeholder
s1 = ROOT.TMarker(-90,0.5,29)
s2 = ROOT.TMarker(0,0.5,29)
s3 = ROOT.TMarker(90,0.5,29)
s4 = ROOT.TMarker(-90,0.441,29)
s5 = ROOT.TMarker(0,0.441,29)
s6 = ROOT.TMarker(90,0.441,29)
s7 = ROOT.TMarker(-90,0.385,29)
s8 = ROOT.TMarker(0,0.385,29)
s9 = ROOT.TMarker(90,0.385,29)
s10 = ROOT.TMarker(-90,0.635,29)
s11 = ROOT.TMarker(0,0.635,29)
s12 = ROOT.TMarker(90,0.635,29)
s1.Draw("same")
s2.Draw("same")
s3.Draw("same")
s4.Draw("same")
s5.Draw("same")
s6.Draw("same")
s7.Draw("same")
s8.Draw("same")
s9.Draw("same")
s10.Draw("same")
s11.Draw("same")
s12.Draw("same")
    
l1 = ROOT.TLegend(0.6,0.7,0.89,0.89)
l1.AddEntry(c1_300,"7 years (staged)","L")
l1.AddEntry(c1_556,"10 years (staged)","L")
l1.AddEntry(c1_984,"15 years (staged)","L")
l1.AddEntry(box1, "NuFit 2016 90% C.L.", "F")
l1.AddEntry(s1, "\"True\" Value","P")
l1.SetBorderSize(0)
l1.SetFillStyle(0)
l1.Draw("same")

ROOT.gPad.RedrawAxis()

outname = "plots/bubbles_q23_2017.eps"
c1.SaveAs(outname)
