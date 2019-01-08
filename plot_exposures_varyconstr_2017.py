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
cpvlist75_ref_short = [0]
cpvlist50_ref_short = [0]
cpvlistbest_ref_short = [0]
mhlist_ref_short = [0]
mhlistbest_ref_short = [0]

cpvlist50_optimized_long = [0]
cpvlist75_optimized_long = [0]
cpvlistbest_optimized_long = [0]
mhlist_optimized_long = [0]
mhlistbest_optimized_long = [0]


for myexp in explist:

      if (myexp==0):
            continue

      #Only solar constraints
      filename = "root/sens_optimized_long_"+hier+"_noconstr_exp"+str(myexp)+".root"
      f1 = ROOT.TFile(filename)
      cpvgraph_short = f1.Get("CPVSig")
      mhgraph_short = f1.Get("MHSig")
      nvals = cpvgraph_short.GetN()
      cpv_vals = [ROOT.Double(0.0)]*nvals
      cpv_vals = array('d',cpv_vals)
      cpv_vals = cpvgraph_short.GetY()

      mh_vals = [ROOT.Double(0.0)]*nvals
      mh_vals = array('d',mh_vals)
      mh_vals = mhgraph_short.GetY()

      i = 0
      cpv_vals_short = []
      mh_vals_short = []
      while i < nvals:
            cpv_vals_short.append(cpv_vals[i])
            mh_vals_short.append(mh_vals[i])
            i += 1

      cpvsig_75_short = sorted(cpv_vals_short)[24]
      cpvsig_50_short = sorted(cpv_vals_short)[49]
      mhsig_100_short = min(mh_vals_short)
      cpvlist75_ref_short.append(cpvsig_75_short)
      cpvlist50_ref_short.append(cpvsig_50_short)
      cpvlistbest_ref_short.append(cpv_vals[26])
      mhlist_ref_short.append(mhsig_100_short)
      mhlistbest_ref_short.append(mh_vals[26])
      f1.Close()

      #Optimized long
      filename = "root/sens_optimized_long_"+hier+"_exp"+str(myexp)+".root"
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
      mhsig_100_optimized_long = min(mh_vals_optimized_long)
      cpvlist75_optimized_long.append(cpvsig_75_optimized_long)
      cpvlist50_optimized_long.append(cpvsig_50_optimized_long)
      cpvlistbest_optimized_long.append(cpv_vals[26])
      mhlist_optimized_long.append(mhsig_100_optimized_long)
      mhlistbest_optimized_long.append(mh_vals[26])
      f1.Close()


n = len(explist)
explist = array('d',explist)
cpvlist75_ref_short = array('d',cpvlist75_ref_short)
cpvlist75_optimized_long = array('d',cpvlist75_optimized_long)

cpvlist50_ref_short = array('d',cpvlist50_ref_short)
cpvlist50_optimized_long = array('d',cpvlist50_optimized_long)

cpvlistbest_ref_short = array('d',cpvlistbest_ref_short)
cpvlistbest_optimized_long = array('d',cpvlistbest_optimized_long)

mhlist_ref_short = array('d',mhlist_ref_short)
mhlist_optimized_long = array('d',mhlist_optimized_long)

mhlistbest_ref_short = array('d',mhlistbest_ref_short)
mhlistbest_optimized_long = array('d',mhlistbest_optimized_long)

g_cpvsig_75_ref_short = ROOT.TGraph(n,explist,cpvlist75_ref_short)
g_cpvsig_75_optimized_long = ROOT.TGraph(n,explist,cpvlist75_optimized_long)

g_cpvsig_50_ref_short = ROOT.TGraph(n,explist,cpvlist50_ref_short)
g_cpvsig_50_optimized_long = ROOT.TGraph(n,explist,cpvlist50_optimized_long)

g_cpvsig_best_ref_short = ROOT.TGraph(n,explist,cpvlistbest_ref_short)
g_cpvsig_best_optimized_long = ROOT.TGraph(n,explist,cpvlistbest_optimized_long)

g_mhsig_100_ref_short = ROOT.TGraph(n,explist,mhlist_ref_short)
g_mhsig_100_optimized_long = ROOT.TGraph(n,explist,mhlist_optimized_long)

g_mhsig_best_ref_short = ROOT.TGraph(n,explist,mhlistbest_ref_short)
g_mhsig_best_optimized_long = ROOT.TGraph(n,explist,mhlistbest_optimized_long)

g_cpvsig_75_ref_short.SetLineWidth(3)
g_cpvsig_75_ref_short.SetLineStyle(2)
g_cpvsig_75_optimized_long.SetLineWidth(3)

g_cpvsig_50_ref_short.SetLineWidth(3)
g_cpvsig_50_ref_short.SetLineStyle(2)
g_cpvsig_50_optimized_long.SetLineWidth(3)

g_cpvsig_best_optimized_long.SetLineWidth(3)
g_cpvsig_best_ref_short.SetLineWidth(3)
g_cpvsig_best_ref_short.SetLineStyle(2)

g_mhsig_100_ref_short.SetLineWidth(3)
g_mhsig_100_ref_short.SetLineStyle(2)
g_mhsig_100_optimized_long.SetLineWidth(3)
g_mhsig_best_optimized_long.SetLineWidth(3)
g_mhsig_best_ref_short.SetLineWidth(3)
g_mhsig_best_ref_short.SetLineStyle(2)

myout = ROOT.TFile("root/exposure_graphs.root","recreate")
g_cpvsig_75_ref_short.SetName("cpvsig75_ref")
g_cpvsig_50_ref_short.SetName("cpvsig50_ref")
g_mhsig_100_ref_short.SetName("mhsig100_ref")
g_cpvsig_75_optimized_long.SetName("cpvsig75_opt")
g_cpvsig_50_optimized_long.SetName("cpvsig50_opt")
g_mhsig_100_optimized_long.SetName("mhsig100_opt")
g_cpvsig_75_ref_short.Write()
g_cpvsig_50_ref_short.Write()
g_mhsig_100_ref_short.Write()
g_cpvsig_75_optimized_long.Write()
g_cpvsig_50_optimized_long.Write()
g_mhsig_100_optimized_long.Write()
myout.Close()

graph_cpvrange75 = filldiff(g_cpvsig_75_optimized_long,g_cpvsig_75_ref_short)
graph_cpvrange50 = filldiff(g_cpvsig_50_optimized_long,g_cpvsig_50_ref_short)
graph_cpvbestrange = filldiff(g_cpvsig_best_optimized_long,g_cpvsig_best_ref_short)
graph_mhrange = filldiff(g_mhsig_100_optimized_long,g_mhsig_100_ref_short)
graph_mhbestrange = filldiff(g_mhsig_best_optimized_long,g_mhsig_best_ref_short)


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
g_cpvsig_75_ref_short.Draw("L same")
g_cpvsig_75_optimized_long.Draw("L same")

graph_cpvrange50.SetFillColor(ROOT.kCyan-7)
graph_cpvrange50.SetLineWidth(0)
graph_cpvrange50.Draw("F same")
g_cpvsig_50_ref_short.Draw("L same")
g_cpvsig_50_optimized_long.Draw("L same")

graph_cpvbestrange.SetFillColor(ROOT.kPink-3)
graph_cpvbestrange.SetLineWidth(0)
graph_cpvbestrange.Draw("F same")
g_cpvsig_best_ref_short.Draw("L same")
g_cpvsig_best_optimized_long.Draw("L same")

#ROOT.gPad.SetTicks(0,1)
#ROOT.gPad.RedrawAxis()

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

l1 = ROOT.TLegend(0.55,0.72,0.89,0.89)
l1.AddEntry(graph_cpvbestrange, "#delta_{CP} = -#pi/2","F")
l1.AddEntry(graph_cpvrange50, "50% of #delta_{CP} values","F")
l1.AddEntry(graph_cpvrange75, "75% of #delta_{CP} values","F")
l1.AddEntry(g_cpvsig_75_optimized_long,"Nominal Analysis","L")
l1.AddEntry(g_cpvsig_75_ref_short,"#theta_{13} & #theta_{23} unconstrained","L")
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

t3sig = ROOT.TPaveText(10.,3.1,115.,3.7)
t3sig.AddText("3#sigma")
t3sig.SetFillColor(0)
t3sig.SetFillStyle(0)
t3sig.SetBorderSize(0)
t3sig.Draw("same")

t5sig = ROOT.TPaveText(10.,5.1,115.,5.7)
t5sig.AddText("5#sigma")
t5sig.SetFillColor(0)
t5sig.SetFillStyle(0)
t5sig.SetBorderSize(0)
t5sig.Draw("same")

outname = "plots/cpv_exp_varyconstr_"+hier+"_2017.eps"
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
graph_mhbestrange.SetFillColor(ROOT.kPink-3)
graph_mhrange.Draw("F same")
if (hier == "no"):
      graph_mhbestrange.Draw("F same")
g_mhsig_100_ref_short.Draw("L same")
g_mhsig_100_optimized_long.Draw("L same")
g_mhsig_best_ref_short.Draw("L same")
g_mhsig_best_optimized_long.Draw("L same")

t1.Draw("same")

lm1 = ROOT.TLegend(0.55,0.75,0.89,0.89)
if (hier == "no"):
      lm1.AddEntry(graph_mhbestrange, "#delta_{CP} = -#pi/2","F")
      lm1.AddEntry(graph_mhrange, "100% of #delta_{CP} values","F")
else:
      lm1.AddEntry(graph_mhrange, "#delta_{CP} = -#pi/2","F")      
      lm1.AddEntry(0, "= 100% of #delta_{CP} values","")
lm1.AddEntry(g_cpvsig_75_optimized_long,"Nominal Analysis","L")
lm1.AddEntry(g_cpvsig_75_ref_short,"#theta_{13} & #theta_{23} unconstrained","L")      
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

outname = "plots/mh_exp_varyconstr_"+hier+"_2017.eps"
c3.SaveAs(outname)

