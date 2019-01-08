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

f1 = ROOT.TFile("root/Bubbles_exp300.root")
rdcpz1 = f1.Get("dcp01sig")  
rdcpp1 = f1.Get("dcppos1sig")
rdcpn1 = f1.Get("dcpneg1sig")

f2 = ROOT.TFile("root/Bubbles_exp556.root")
rdcpz2 = f2.Get("dcp01sig")  
rdcpp2 = f2.Get("dcppos1sig")
rdcpn2 = f2.Get("dcpneg1sig")

f3 = ROOT.TFile("root/Bubbles_exp984.root")
rdcpz3 = f3.Get("dcp01sig")  
rdcpp3 = f3.Get("dcppos1sig")
rdcpn3 = f3.Get("dcpneg1sig")

nufit = ROOT.TFile("root/nufit_dcpvq13_contours_rotate.root")
h_no = nufit.Get("h_no")

dcpz1 = rotate(rdcpz1)
dcpp1 = rotate(rdcpp1)
dcpn1 = rotate(rdcpn1)

dcpz2 = rotate(rdcpz2)
dcpp2 = rotate(rdcpp2)
dcpn2 = rotate(rdcpn2)

dcpz3 = rotate(rdcpz3)
dcpp3 = rotate(rdcpp3)
dcpn3 = rotate(rdcpn3)

dcpz1.SetLineWidth(3)
dcpp1.SetLineWidth(3)
dcpn1.SetLineWidth(3)
dcpz2.SetLineWidth(3)
dcpp2.SetLineWidth(3)
dcpn2.SetLineWidth(3)
dcpz3.SetLineWidth(3)
dcpp3.SetLineWidth(3)
dcpn3.SetLineWidth(3)

dcpz1.SetLineColor(ROOT.kGreen-7)
dcpp1.SetLineColor(ROOT.kGreen-7)
dcpn1.SetLineColor(ROOT.kGreen-7)

dcpz2.SetLineColor(ROOT.kOrange-3)
dcpp2.SetLineColor(ROOT.kOrange-3)
dcpn2.SetLineColor(ROOT.kOrange-3)

dcpz3.SetLineColor(ROOT.kBlue-7)
dcpp3.SetLineColor(ROOT.kBlue-7)
dcpn3.SetLineColor(ROOT.kBlue-7)

dcpz1.SetContour(1)
dcpz1.SetContourLevel(0,4.61)
dcpn1.SetContour(1)
dcpn1.SetContourLevel(0,4.61)
dcpp1.SetContour(1)
dcpp1.SetContourLevel(0,4.61)
dcpz2.SetContour(1)
dcpz2.SetContourLevel(0,4.61)
dcpn2.SetContour(1)
dcpn2.SetContourLevel(0,4.61)
dcpp2.SetContour(1)
dcpp2.SetContourLevel(0,4.61)
dcpz3.SetContour(1)
dcpz3.SetContourLevel(0,4.61)
dcpn3.SetContour(1)
dcpn3.SetContourLevel(0,4.61)
dcpp3.SetContour(1)
dcpp3.SetContourLevel(0,4.61)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(-180, 0.07, 180., 0.11)
h1.GetYaxis().SetTitle("sin^{2}2#theta_{13}")
h1.GetXaxis().SetTitle("#delta_{CP} (degrees)")
h1.GetYaxis().SetTitleOffset(1.7)
c1.Modified()

h_no.Draw("cont0 same")
h_no.SetContour(2)
h_no.SetContourLevel(0,0)
h_no.SetContourLevel(1,4.61)
colors = [ROOT.kYellow-7]
colors = array('i',colors)
ROOT.gStyle.SetPalette(1,colors)

#Not to plot, just for the legend
box1 = ROOT.TBox(41.1,-180,43.8,120)
box1.SetFillColor(ROOT.kYellow-7)
box1.SetLineWidth(0)

dcpz1.Draw("cont3 same")
dcpp1.Draw("cont3 same")
dcpn1.Draw("cont3 same")
dcpz2.Draw("cont3 same")
dcpp2.Draw("cont3 same")
dcpn2.Draw("cont3 same")
dcpz3.Draw("cont3 same")
dcpp3.Draw("cont3 same")
dcpn3.Draw("cont3 same")

s1 = ROOT.TMarker(-90.,0.085,29)
s2 = ROOT.TMarker(0.0,0.085,29)
s3 = ROOT.TMarker(90.,0.085,29)
s1.Draw("same")
s2.Draw("same")
s3.Draw("same")

t1 = ROOT.TPaveText(0.16,0.75,0.45,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("Normal Ordering")
t1.AddText("sin^{2}#theta_{23} = 0.441 #pm 0.042")
t1.AddText("90% C.L. (2 d.o.f.)")
t1.SetFillStyle(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.6,0.7,0.89,0.89)
l1.AddEntry(dcpz1,"7 years (staged)","L")
l1.AddEntry(dcpz2,"10 years (staged)","L")
l1.AddEntry(dcpz3,"15 years (staged)","L")
l1.AddEntry(box1, "NuFit 2016 90% C.L.", "F")
l1.AddEntry(s1, "\"True\" Value","P")
l1.SetBorderSize(0)
l1.SetFillStyle(0)
l1.Draw("same")
ROOT.gPad.RedrawAxis()

outname = "plots/bubbles_q13_2017.eps"
c1.SaveAs(outname)

