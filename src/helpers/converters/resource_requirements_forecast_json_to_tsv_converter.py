import io

class Converter:
    _forecast = None
    #_includeHeaders = True
    
    def __init__(self, forecast):
        self.__class__._forecast = forecast    
        


    @classmethod
    def All(cls, includeHeaders:bool = True):
        
        if cls._forecast is None:
            return str()

        sb = io.StringIO()
        
        sb.write(Converter.FinancialStats() + "\n\n")
        sb.write(Converter.HardwareStats()+ "\n\n" )
        sb.write(Converter.SoftwareStats() + "\n\n")
        sb.write(Converter.FacilityStats()+ "\n\n" )


        sb.write(Converter.FinancialSummary(includeHeaders) + "\n\n")
        
        sb.write(Converter.HardwareSummary(includeHeaders)+ "\n\n" )
        sb.write(Converter.HardwareDetail(includeHeaders)+ "\n\n" )

        sb.write(Converter.SoftwareSummary(includeHeaders) + "\n\n")
        sb.write(Converter.SoftwareDetail(includeHeaders)+ "\n\n" )

        sb.write(Converter.FacilitySummary(includeHeaders) + "\n\n")
        sb.write(Converter.FacilityDetail(includeHeaders)+ "\n\n" )

        return sb.getvalue()


    @classmethod
    def FinancialStats(cls):
        
        fs = cls._forecast.FinancialStats
        if fs is None:
            return str()      

        sb = io.StringIO()
        
        sb.write("Total Cost" + "\t" + str(fs.TotalCost ) + "\n" ) 
        sb.write("Total Cost Per Year" + "\t" + str(fs.TotalCostPerYear ) + "\n" ) 
        sb.write("Kratio" + "\t" + str(fs.Kratio ) + "\n" ) 
        sb.write("Kratio Shift" + "\t" + str(fs.KratioShift ) + "\n" ) 
        sb.write("Server Unit Cost" + "\t" + str(fs.ServerUnitCost ) + "\n" ) 
        sb.write("Server Hour Nominal" + "\t" + str(fs.ServerHourNominal ) + "\n" ) 
        sb.write("Server Hour Real" + "\t" + str(fs.ServerHourReal ) + "\n" ) 
        sb.write("Processor Unit Cost" + "\t" + str(fs.ProcessorUnitCost ) + "\n" ) 
        sb.write("Processor Hour Nominal" + "\t" + str(fs.ProcessorHourNominal ) + "\n" ) 
        sb.write("Processor Hour Real" + "\t" + str(fs.ProcessorHourReal ) + "\n" ) 
        sb.write("Core Unit Cost" + "\t" + str(fs.CoreUnitCost ) + "\n" ) 
        sb.write("Core Hour Nominal" + "\t" + str(fs.CoreHourNominal ) + "\n" ) 
        sb.write("Core Hour Real" + "\t" + str(fs.CoreHourReal ) + "\n" ) 
    
        return sb.getvalue()

    @classmethod
    def HardwareStats(cls):

        hs = cls._forecast.HardwareStats
        if hs is None:
            return str()      
        
        sb = io.StringIO()

        sb.write("Performance Capture Yield" + "\t" + str(hs.PerfCaptureYield) + "\n")
        sb.write("Avg Utilization" + "\t" + str(hs.AvgUtilization) + "\n")
        sb.write("Annual Removal Percent" + "\t" + str(hs.AnnualRemovalPercent) + "\n")
        sb.write("Annual Add Percent" + "\t" + str(hs.AnnualAddPercent) + "\n")
        sb.write("Server Avg Age" + "\t" + str(hs.ServerAvgAge) + "\n")
        sb.write("Server Avg Removal Age" + "\t" + str(hs.ServerAvgRemovalAge) + "\n")
        sb.write("Server Avg Qty" + "\t" + str(hs.ServerAvgQty) + "\n")
        sb.write("Server Max Qty" + "\t" + str(hs.ServerMaxQty) + "\n")
        sb.write("Server Max Qty Time" + "\t" + str(hs.ServerMaxQtyTime) + "\n")
        sb.write("Server Avg Perf" + "\t" + str(hs.ServerAvgPerf) + "\n")
        sb.write("Processor Avg Qty" + "\t" + str(hs.ProcessorAvgQty) + "\n")
        sb.write("Processor Max Qty" + "\t" + str(hs.ProcessorMaxQty) + "\n")
        sb.write("Processor Max Qty Time" + "\t" + str(hs.ProcessorMaxQtyTime) + "\n")
        sb.write("Processor Avg Perf" + "\t" + str(hs.ProcessorAvgPerf) + "\n")
        sb.write("Core Avg Qty" + "\t" + str(hs.CoreAvgQty) + "\n")
        sb.write("Core Max Qty" + "\t" + str(hs.CoreMaxQty) + "\n")
        sb.write("Core Max Qty Time" + "\t" + str(hs.CoreMaxQtyTime) + "\n")
        sb.write("Core Avg Perf" + "\t" + str(hs.CoreAvgPerf) + "\n")
    
        return sb.getvalue()


    @classmethod
    def SoftwareStats(cls):

        ss = cls._forecast.SoftwareStats
        if ss is None:
            return str()      

        sb = io.StringIO()

        sb.write("Server Licenses Utilization" + "\t" + str(ss.ServerLicensesUtilization) + "\n")
        sb.write("Server Avg Excess Licenses" + "\t" + str(ss.ServerAvgExcessLicenses) + "\n")
        sb.write("Server Peak Excess Licenses" + "\t" + str(ss.ServerPeakExcessLicenses) + "\n")
        sb.write("Processor Licenses Utilization" + "\t" + str(ss.ProcessorLicensesUtilization) + "\n")
        sb.write("Processor Avg Excess Licenses" + "\t" + str(ss.ProcessorAvgExcessLicenses) + "\n")
        sb.write("Processor Peak Excess Licenses" + "\t" + str(ss.ProcessorPeakExcessLicenses) + "\n")
        sb.write("Core Licenses Utilization" + "\t" + str(ss.CoreLicensesUtilization) + "\n")
        sb.write("Core Avg Excess Licenses" + "\t" + str(ss.CoreAvgExcessLicenses) + "\n")
        sb.write("Core Peak Excess Licenses" + "\t" + str(ss.CorePeakExcessLicenses) + "\n")
    
        return sb.getvalue()


    @classmethod
    def FacilityStats(cls):

        fs = cls._forecast.FacilityStats
        if fs is None:
            return str()      

        sb = io.StringIO()

        sb.write("Avg Number of 1U Rack Units" + "\t" + str(fs.RackUnitAvgSlots) + "\n")
        sb.write("Rack Units APC" + "\t" + str(fs.RackUnitSlotsAnnualizedChangePercent) + "\n")
        sb.write("Capacity per RU APC" + "\t" + str(fs.CapacityPerRackSlotAnnualizedChangePercent) + "\n")
        sb.write("kWh per Capacity APC" + "\t" + str(fs.KWhPerCapacityUnitAnnualizedChangePercent) + "\n")
        sb.write("kWh per RU APC" + "\t" + str(fs.KWhPerRackUnitSlotAnnualizedChangePercent) + "\n")
    
        return sb.getvalue()



    @classmethod
    def FinancialSummary(cls, includeHeaders=True):

        lst = cls._forecast.FinancialSummary
        
        if lst is None or len(lst) == 0:
            return str()      


        sb = io.StringIO()      # string builder for individual lines
        header1 = "\t  \t  \t  \t  \t  Incremental Costs  \t  \t  \t  \t  \t  \t  \t  \t  \t  Total Costs"
        header2 = "Interval Nbr  \t  Time Start  \t  Time End  \t  Date Start  \t  Date End  \t  Server \t  Assignment  \t  Perpetual Lic \
                   \t  Support  \t  Subscription  \t  Power  \t  Facility \t  Total  \t  \t  Server  \t  Assignment  \t  Perpetual Lic  \t  Support \t  \
                   Subscription  \t  Power  \t  Facility  \t  Total  \t Total Per Perf  \t  Annualized Total  \t  Annualized Cost Per Perf  \t  Kratio"          
        
        # note about header string - python seems to include all white space in copy/paste operation into excel (i.e., cell values include any preceding space before value)
        # remove whitespace
        
        header1 = header1.replace(" ", "")
        header2 = header2.replace(" ", "")
        
        if includeHeaders is True:
            sb.write(header1 + "\n")
            sb.write(header2 + "\n")

        for i in range(len(lst)): 
            
            item = io.StringIO()    # string builder for items in a line  
                
            item.write(str(lst[i].IntervalNbr) + "\t")
            item.write(str(lst[i].TimeStart) + "\t")
            item.write(str(lst[i].TimeEnd) + "\t")
            item.write(str(lst[i].DateStart) + "\t")
            item.write(str(lst[i].DateEnd) + "\t")
            item.write(str(lst[i].ServerIncCost) + "\t")
            item.write(str(lst[i].AssignmentIncCost) + "\t")
            item.write(str(lst[i].PerpetualLicenseIncCost) + "\t")
            item.write(str(lst[i].SupportIncCost) + "\t")
            item.write(str(lst[i].SubscriptionIncCost) + "\t")
            item.write(str(lst[i].PowerIncCost) + "\t")
            item.write(str(lst[i].FacilityIncCost) + "\t")
            item.write(str(lst[i].TotalIncCost) + "\t")
            item.write("\t")
            item.write(str(lst[i].ServerCumCost) + "\t")
            item.write(str(lst[i].AssignmentCumCost) + "\t")
            item.write(str(lst[i].PerpetualLicenseCumCost) + "\t")
            item.write(str(lst[i].SupportCumCost) + "\t")
            item.write(str(lst[i].SubscriptionCumCost) + "\t")
            item.write(str(lst[i].PowerCumCost) + "\t")
            item.write(str(lst[i].FacilityCumCost) + "\t")
            item.write(str(lst[i].TotalCumCost) + "\t")
            item.write(str(lst[i].TotalCostPerPerf) + "\t")
            item.write(str(lst[i].AnnualizedTotalCost) + "\t")
            item.write(str(lst[i].AnnualizedTotalCostPerPerf) + "\t")
            item.write(str(lst[i].Kratio))
    
            sb.write(item.getvalue() + "\n")                #   join items into a single, tab-seperated line and
                                                            #   add to line string builder
            
        return sb.getvalue()
        
    
    @classmethod
    def HardwareSummary(cls, includeHeaders=True):
        
        lst = cls._forecast.HardwareSummary       
        if lst is None or len(lst) == 0:
            return str()  
        
        sb = io.StringIO()      # string builder for individual lines
        header1 = "\t  \t  \t  \t  \t  \t  \t  \t   \t  \t Incremental Quantities \t \t  \t  \t  \t Cumulative Quantities"
        header2 = "Interval Nbr \t Time Start \t Time End \t Date Start \t Date End \t Demand Start \t Demand Delta \t Demand End \t Util Start \t Util End \t Server \t Processor \t Core \t Perf \t \t Server \t Processor \t Core \t Perf \t Server Perf \t Proc Perf \t Core Perf \t Svr Avg Age \t Svr Avg Remove Age \t Add % \t Remove % \t Perf Capture Rate"


        header1 = header1.replace(" ", "")
        header2 = header2.replace(" ", "")


        if includeHeaders is True:
            sb.write(header1 + "\n")
            sb.write(header2 + "\n")

        for i in range(len(lst)): 
            
            item = io.StringIO()    # string builder for items in a line  
                
            item.write(str(lst[i].IntervalNbr) + "\t")
            item.write(str(lst[i].TimeStart ) + "\t" )
            item.write(str(lst[i].TimeEnd ) + "\t" )
            item.write(str(lst[i].DateStart ) + "\t" )
            item.write(str(lst[i].DateEnd ) + "\t" )
            item.write(str(lst[i].DemandStart ) + "\t" )
            item.write(str(lst[i].DemandDelta ) + "\t" )
            item.write(str(lst[i].DemandEnd ) + "\t" )
            item.write(str(lst[i].UtilizationStart ) + "\t" )
            item.write(str(lst[i].UtilizationEnd ) + "\t" )
            item.write(str(lst[i].ServerIncQty ) + "\t" )
            item.write(str(lst[i].ProcessorIncQty ) + "\t" )
            item.write(str(lst[i].CoreIncQty ) + "\t" )
            item.write(str(lst[i].PerfInc ) + "\t" )
            item.write("\t")
            item.write(str(lst[i].ServerQty ) + "\t" )
            item.write(str(lst[i].ProcessorQty ) + "\t" )
            item.write(str(lst[i].CoreQty ) + "\t" )
            item.write(str(lst[i].PerfTotal ) + "\t" )
            item.write(str(lst[i].ServerPerf ) + "\t" )
            item.write(str(lst[i].ProcessorPerf ) + "\t" )
            item.write(str(lst[i].CorePerf ) + "\t" )
            item.write(str(lst[i].ServerAvgAge ) + "\t" )
            item.write(str(lst[i].ServerAvgRemovalAge ) + "\t" )
            item.write(str(lst[i].TransactionPercentAdd ) + "\t" )
            item.write(str(lst[i].TransactionPercentRemove ) + "\t" )
            item.write(str(lst[i].PerfCaptureRate))
    
            sb.write(item.getvalue() + "\n")                #   join items into a single, tab-seperated line and
                                                            #   add to line string builder
            
        return sb.getvalue()

    @classmethod
    def HardwareDetail(cls, includeHeaders=True):

        lst = cls._forecast.HardwareDetail
        if lst is None or len(lst) == 0:
            return str()  
        
        sb = io.StringIO()      # string builder for individual lines
        
        header1 = "\t Source  \t  \t  \t  \t  \t  \t  \t Quantities  \t  \t  \t  \t  Performance Rating (Perf) \t   \t  \t  \t  \t Configuration (Sizes)  \t  \t  \t  \t  \t  \t Transaction"
        header2 = "Interval Nbr \t Interval Nbr \t Identifier \t Time Start \t Time End \t Date Start \t Date End \t \t Server \t Processor \t Core \t \t Trans Total \t Server \t Processor \t Core \t \t Process Set \t Core Set \t Rack Unit \t Watts \t \t Total kWh \t Residual Value"

        header1 = header1.replace(" ", "")
        header2 = header2.replace(" ", "")


        if includeHeaders is True:
            sb.write(header1 + "\n")
            sb.write(header2 + "\n")

        for i in range(len(lst)): 
            
            item = io.StringIO()    # string builder for items in a line  
                
            item.write(str(lst[i].IntervalNbr ) + "\t" )
            item.write(str(lst[i].SourceIntervalNbr ) + "\t" )
            item.write(str(lst[i].UniqueIdentifier ) + "\t" )
            item.write(str(lst[i].TimeStart ) + "\t" )
            item.write(str(lst[i].TimeEnd ) + "\t" )
            item.write(str(lst[i].DateStart ) + "\t" )
            item.write(str(lst[i].DateEnd ) + "\t" )
            item.write("\t")
            item.write(str(lst[i].ServerQty ) + "\t" )
            item.write(str(lst[i].ProcessorQty ) + "\t" )
            item.write(str(lst[i].CoreQty ) + "\t" )
            item.write("\t")
            item.write(str(lst[i].PerfTotal ) + "\t" )
            item.write(str(lst[i].ServerPerf ) + "\t" )
            item.write(str(lst[i].ProcessorPerf ) + "\t" )
            item.write(str(lst[i].CorePerf ) + "\t" )
            item.write("\t")
            item.write(str(lst[i].ProcessorSetSize ) + "\t" )
            item.write(str(lst[i].CoreSetSize ) + "\t" )
            item.write(str(lst[i].ServerSize ) + "\t" )
            item.write(str(lst[i].WattsRating ) + "\t" )
            item.write("\t")
            item.write(str(lst[i].TotalKilowattHrs ) + "\t" )
            item.write(str(lst[i].TransactionResidualValue ) + "\t" )
    
            sb.write(item.getvalue() + "\n")                #   join items into a single, tab-seperated line and
                                                            #   add to line string builder
            
        return sb.getvalue()


    @classmethod
    def FacilitySummary(cls, includeHeaders=True):

        lst = cls._forecast.FacilitySummary
        if lst is None or len(lst) == 0:
            return str()  
                
        sb = io.StringIO()      # string builder for individual lines
        header1 = "\t  \t  \t  \t  \t Rack Units (1U)  \t  \t \t \t Kilowatt Hrs"
        header2 = "Interval Nbr \t Time Start \t Time End \t Date Start \t Date End \t Incremental \t Cumulative \t Perf per RU \t \t Incremental \t Annualized \t Per Perf Unit \t Per RU"

        header1 = header1.replace(" ", "")
        header2 = header2.replace(" ", "")

        if includeHeaders is True:
            sb.write(header1 + "\n")
            sb.write(header2 + "\n")

        for i in range(len(lst)): 
            
            item = io.StringIO()    # string builder for items in a line  
                
            item.write(str(lst[i].IntervalNbr) + "\t" )
            item.write(str(lst[i].TimeStart) + "\t" )
            item.write(str(lst[i].TimeEnd) + "\t" )
            item.write(str(lst[i].DateStart) + "\t" )
            item.write(str(lst[i].DateEnd) + "\t" )
            item.write(str(lst[i].RackUnitSlotQtyInc) + "\t" ) 
            item.write(str(lst[i].RackUnitSlotQtyCum) + "\t" )
            item.write(str(lst[i].ComputeCapacityPerRackUnitSlot) + "\t" )
            item.write("\t")
            item.write(str(lst[i].KilowattHrsInc) + "\t" )
            item.write(str(lst[i].KilowattHrsAnnualized) + "\t" )
            item.write(str(lst[i].KilowattHrsAnnualizedPerCapacityUnit) + "\t" )
            item.write(str(lst[i].KilowattHrsAnnualizedPerRackUnitSlot) + "\t" )
    
            sb.write(item.getvalue() + "\n")                #   join items into a single, tab-seperated line and
                                                            #   add to line string builder
            
        return sb.getvalue()


    @classmethod
    def FacilityDetail(cls, includeHeaders=True):
                
        lst = cls._forecast.FacilityDetail
        if lst is None or len(lst) == 0:
            return str()  
        

        sb = io.StringIO()      # string builder for individual lines
        header1 = "\t  \t  \t  \t  \t   \t Rack Units (1U)  \t  \t  \t \t Server Configuration"
        header2 = "Interval Nbr \t Time Start \t Time End \t Date Start \t Date End \t Source Interval Nbr \t Incremental \t Cumulative \t Total kWhrs \t \t Proc Set Size \t Core Set Size \t Total Watts \t RU Size "

        header1 = header1.replace(" ", "")
        header2 = header2.replace(" ", "")

        if includeHeaders is True:
            sb.write(header1 + "\n")
            sb.write(header2 + "\n")

        for i in range(len(lst)): 
            
            item = io.StringIO()    # string builder for items in a line  
                
            item.write(str(lst[i].IntervalNbr) + "\t" )
            item.write(str(lst[i].TimeStart) + "\t" )
            item.write(str(lst[i].TimeEnd) + "\t" )
            item.write(str(lst[i].DateStart) + "\t" )
            item.write(str(lst[i].DateEnd) + "\t" )
            item.write(str(lst[i].SourceIntervalNbr) + "\t" )
            item.write(str(lst[i].RackUnitSlotQtyInc) + "\t" ) 
            item.write(str(lst[i].RackUnitSlotQtyCum) + "\t" )
            item.write(str(lst[i].TotalKilowattHrs) + "\t" )
            item.write("\t")
            item.write(str(lst[i].ProcessorSetSize) + "\t" )
            item.write(str(lst[i].CoreSetSize) + "\t" )
            item.write(str(lst[i].TotalWatts) + "\t" )
            item.write(str(lst[i].ServerSize) + "\t" )
                
            sb.write(item.getvalue() + "\n")                #   join items into a single, tab-seperated line and
                                                            #   add to line string builder
            
        return sb.getvalue()



    @classmethod
    def SoftwareSummary(cls, includeHeaders=True):
                
        lst = cls._forecast.SoftwareSummary
        if lst is None or len(lst) == 0:
            return str()  
        

        sb = io.StringIO()      # string builder for individual lines
        header1 = "\t \t \t \t \t Server Licenses \t \t \t \t \t \t Processor Licenses \t \t \t \t \t \t Core Licenses"
        header2 = "Interval Nbr \t Time Start \t Time End \t Date Start \t Date End \t Stack Qty \t Required Qty \t Avail Qty \t Utilization \t \t Stack Qty \t Required Qty \t Avail Qty \t Utilization \t \t Stack Qty \t Required Qty \t Avail Qty \t Utilization"

        header1 = header1.replace(" ", "")
        header2 = header2.replace(" ", "")

        if includeHeaders is True:
            sb.write(header1 + "\n")
            sb.write(header2 + "\n")

        for i in range(len(lst)): 
            
            item = io.StringIO()    # string builder for items in a line  
                
            item.write(str(lst[i].IntervalNbr) + "\t" )
            item.write(str(lst[i].TimeStart) + "\t" )
            item.write(str(lst[i].TimeEnd) + "\t" )
            item.write(str(lst[i].DateStart) + "\t" )
            item.write(str(lst[i].DateEnd) + "\t" )
            item.write(str(lst[i].ServerStackQty) + "\t" )
            item.write(str(lst[i].ServerRequiredQty) + "\t" )
            item.write(str(lst[i].ServerAvailableQty) + "\t" )
            item.write(str(lst[i].ServerUtilization) + "\t" )
            item.write("\t")
            item.write(str(lst[i].ProcessorStackQty) + "\t" )
            item.write(str(lst[i].ProcessorRequiredQty) + "\t" )
            item.write(str(lst[i].ProcessorAvailableQty) + "\t" )
            item.write(str(lst[i].ProcessorUtilization) + "\t" )
            item.write("\t")
            item.write(str(lst[i].CoreStackQty) + "\t" )
            item.write(str(lst[i].CoreRequiredQty) + "\t" )
            item.write(str(lst[i].CoreAvailableQty) + "\t" )
            item.write(str(lst[i].CoreUtilization) + "\t" )
    
            sb.write(item.getvalue() + "\n")                #   join items into a single, tab-seperated line and
                                                            #   add to line string builder
            
        return sb.getvalue()


    @classmethod
    def SoftwareDetail(cls, includeHeaders=True):

        lst = cls._forecast.SoftwareDetail
        if lst is None or len(lst) == 0:
            return str()  
        
        
        sb = io.StringIO()      # string builder for individual lines
        header1 = "\t \t \t \t \t \t \t License Attributes \t \t \t \t Quantities"
        header2 = "License Id \t Interval Nbr \t Time Start \t Time End \t Date Start \t Date End \t \t Type \t Metric \t Contract \t \t Required \t Available \t Excess"

        header1 = header1.replace(" ", "")
        header2 = header2.replace(" ", "")

        if includeHeaders is True:
            sb.write(header1 + "\n")
            sb.write(header2 + "\n")

        for i in range(len(lst)): 
            
            item = io.StringIO()    # string builder for items in a line  
                
            item.write(str(lst[i].LicenseId) + "\t" )
            item.write(str(lst[i].IntervalNbr) + "\t" )
            item.write(str(lst[i].TimeStart) + "\t" )
            item.write(str(lst[i].TimeEnd) + "\t" )
            item.write(str(lst[i].DateStart) + "\t" )
            item.write(str(lst[i].DateEnd) + "\t" )
            item.write("\t")
            item.write(str(lst[i].LicenseType) + "\t" )
            item.write(str(lst[i].LicenseMetric) + "\t" )
            item.write(str(lst[i].ContractType) + "\t" )
            item.write("\t")
            item.write(str(lst[i].Required) + "\t" )
            item.write(str(lst[i].Available) + "\t" )
            item.write(str(lst[i].Excess) + "\t" )
    
            sb.write(item.getvalue() + "\n")                #   join items into a single, tab-seperated line and
                                                            #   add to line string builder
            
        return sb.getvalue()
    
    


    