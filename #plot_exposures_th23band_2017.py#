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

g_cpvsig_75_nom.SetLineWidth(3)
g_cpvsig_75_nom.SetLineStyle(2)
g_cpvsig_50_nom.SetLineWidth(3)
g_cpvsig_50_nom.SetLineStyle(2)
g_cpvsig_best_nom.SetLineWidth(3)
g_cpvsig_best_nom.SetLineStyle(2)
g_mhsig_nom.SetLineWidth(3)
g_mhsig_nom.SetLineStyle(2)
g_mhsig_best_nom.SetLineWidth(3)
g_mhsig_best_nom.SetLineStyle(2)

myout = ROOT.TFile("root/exposure_graphs_"+hier+".root","recreate")
g_cpvsig_75_lo.SetName("cpvsig75_lo")
g_cpvsig_50_lo.SetName("cpvsig50_lo")
g_cpvsig_best_lo.SetName("cpvsigbest_lo")
g_mhsig_lo.SetName("mhsig_lo")
g_mhsig_best_lo.SetName("mhsig_best_lo")

g_cpvsig_75_hi.SetName("cpvsig75_hi")
g_cpvsig_50_hi.SetName("cpvsig50_hi")
g_cpvsig_best_hi.SetName("cpvsigbest_hi")
g_mhsig_hi.SetName("mhsig_hi")
g_mhsig_best_hi.SetName("mhsig_best_hi")

g_cpvsig_75_nom.SetName("cpvsig75_nom")
g_cpvsig_50_nom.SetName("cpvsig50_nom")
g_cpvsig_best_nom.SetName("cpvsigbest_nom")
g_mhsig_nom.SetName("mhsig_nom")
g_mhsig_best_nom.SetName("mhsig_best_nom")

g_cpvsig_75_lo.Write()
g_cpvsig_50_lo.Write()
g_cpvsig_best_lo.Write()
g_mhsig_lo.Write()
g_mhsig_best_lo.Write()

g_cpvsig_75_hi.Write()
g_cpvsig_50_hi.Write()
g_cpvsig_best_hi.Write()
g_mhsig_hi.Write()
g_mhsig_best_hi.Write()

g_cpvsig_75_nom.Write()
g_cpvsig_50_nom.Write()
g_cpvsig_best_nom.Write()
g_mhsig_nom.Write()
g_mhsig_best_nom.Write()

myout.Close()

graph_cpvrange75 = filldiff(g_cpvsig_75_lo,g_cpvsig_75_hi)
graph_cpvrange50 = filldiff(g_cpvsig_50_lo,g_cpvsig_50_hi)
graph_cpvbestrange = filldiff(g_cpvsig_best_lo,g_cpvsig_best_hi)
graph_mhrange = filldiff(g_mhsig_hi,g_mhsig_lo)
graph_mhbestrange = filldiff(g_mhsig_best_hi,g_mhsig_best_lo)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0,0.0,1500.0,14.0)
h1.SetTitle("CP Violation Sensitivity")
h1.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h1.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h1.GetYaxis().SetTitleOffset(1.3)
h1.GetYaxis().CenterTitle()
c1.Modified()
graph_cpvrange75.SetFillColor(ROOT.kCyan+2)
graph_cpvrange75.SetLineWidth(0)
graph_cpvrange75.Draw("F same")
g_cpvsig_75_nom.Draw("L same")

graph_cpvrange50.SetFillColor(ROOT.kCyan-7)
graph_cpvrange50.SetLineWidth(0)
graph_cpvrange50.Draw("F same")
g_cpvsig_50_nom.Draw("L same")

graph_cpvbestrange.SetFillColor(ROOT.kPink-3)
graph_cpvbestrange.SetLineWidth(0)
graph_cpvbestrange.Draw("F same")
g_cpvsig_best_nom.Draw("L same")

#ROOT.gPad.SetTicks(0,1)
#ROOT.gPad.RedrawAxis()

t1 = ROOT.TPaveText(0.16,0.75,0.53,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText(htext)
t1.AddText("sin^{2}2#theta_{13} = 0.085 #pm 0.003")
t1.AddText("#theta_{23}: NuFit 2016 (90% C.L. range)")
t1.SetFillColor(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.55,0.72,0.89,0.89)
l1.AddEntry(graph_cpvbestrange, "#delta_{CP} = -#pi/2","F")
l1.AddEntry(graph_cpvrange50, "50% of #delta_{CP} values","F")
l1.AddEntry(graph_cpvrange75, "75% of #delta_{CP} values","F")
if (hier == 'no'):
      l1.AddEntry(g_cpvsig_75_nom,"sin^{2}#theta_{23} = 0.441 #pm 0.042", "L")
elif (hier == 'io'):
      l1.AddEntry(g_cpvsig_75_nom,"sin^{2}#theta_{23} = 0.587 #pm 0.043", "L")      
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

t3sig = ROOT.TPaveText(25.,3.1,115.,3.7)
t3sig.AddText("3#sigma")
t3sig.SetFillColor(0)
t3sig.SetFillStyle(0)
t3sig.SetBorderSize(0)
t3sig.Draw("same")

t5sig = ROOT.TPaveText(25.,5.1,115.,5.7)
t5sig.AddText("5#sigma")
t5sig.SetFillColor(0)
t5sig.SetFillStyle(0)
t5sig.SetBorderSize(0)
t5sig.Draw("same")

outname = "plots/cpv_exp_th23band_"+hier+"_2017.eps"
c1.SaveAs(outname)

c3 = ROOT.TCanvas("c3","c3",800,800)
c3.SetLeftMargin(0.15)
h3 = c3.DrawFrame(0,0.0,500.0,15.0)
#ROOT.gPad.SetTicks(0,1)
h3.SetTitle("MH Sensitivity")
h3.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h3.GetYaxis().SetTitle("#sqrt{#bar{#Delta#chi^{2}}}")
h3.GetYaxis().SetTitleOffset(1.3)
h3.GetYaxis().CenterTitle()
c3.Modified()
graph_mhrange.SetFillColor(ROOT.kCyan+3)
graph_mhrange.SetLineWidth(0)
graph_mhbestrange.SetFillColor(ROOT.kPink-3)
graph_mhbestrange.SetLineWidth(0)
graph_mhrange.Draw("F same")
if (hier == 'no'):
      graph_mhbestrange.Draw("F same")
      g_mhsig_best_nom.Draw("L same")
g_mhsig_nom.Draw("L same")

t1.Draw("same")

lm1 = ROOT.TLegend(0.55,0.75,0.89,0.89)
if (hier == 'no'):
      lm1.AddEntry(graph_mhbestrange, "#delta_{CP} = -#pi/2","F")
      lm1.AddEntry(graph_mhrange, "100% of #delta_{CP} values","F")
      lm1.AddEntry(g_mhsig_nom,"sin^{2}#theta_{23} = 0.441 #pm 0.042", "L")      
elif (hier == 'io'):
      lm1.AddEntry(graph_mhrange, "#delta_{CP} = -#pi/2","F")
      lm1.AddEntry(0, "= 100% of #delta_{CP} values","")
      lm1.AddEntry(g_mhsig_nom,"sin^{2}#theta_{23} = 0.587 #pm 0.042", "L")      

lm1.SetBorderSize(0)
lm1.SetFillStyle(0)
lm1.Draw("same")

linem1 = ROOT.TLine(0.,3.,500.,3.)
linem1.SetLineStyle(2)
linem1.SetLineWidth(3)
linem1.Draw("same")

linem2 = ROOT.TLine(0.0,5.,500.,5.)
linem2.SetLineStyle(2)
linem2.SetLineWidth(3)
linem2.Draw("same")

#line1.Draw("same")
#line2.Draw("same")
#t3sig.Draw("same")
#t5sig.Draw("same")

outname = "plots/mh_exp_th23band_"+hier+"_2017.eps"
c3.SaveAs(outname)

