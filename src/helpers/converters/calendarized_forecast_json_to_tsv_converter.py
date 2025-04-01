import io

class Converter:
    _forecast = None
    
    
    def __init__(self, forecast):
        self.__class__._forecast = forecast    
        


    @classmethod
    def All(cls, includeHeaders:bool = True):
        
        sb = io.StringIO()
        cls._includeHeaders = includeHeaders

        sb.write(Converter.FinancialSummary(includeHeaders) + "\n\n")
        sb.write(Converter.HardwareInventory(includeHeaders) + "\n\n")
        sb.write(Converter.HardwareTransactions(includeHeaders) + "\n\n")
        sb.write(Converter.SoftwareInventory(includeHeaders) + "\n\n")
        sb.write(Converter.FacilityResources(includeHeaders) + "\n\n")

        return sb.getvalue()

    @classmethod
    def FinancialSummary(cls, includeHeaders:bool = True):

        lst = cls._forecast.Financial        
        if lst is None or len(lst) == 0:
            return str()      
        

        sb = io.StringIO()      # string builder for individual lines

        header1 =  "Report Period \t \t \t \t \t \t \t \t \t Total \t \t \t Total"
        header2 = "Month \t Nbr \t Start \t End \t Server \t Assignment \t Perpetual Lic \t Support \t Subscription \t Software \t Power \t Facility \t Cost "
        
        header1 = header1.replace("  ", " ")
        header2 = header2.replace("  ", " ")
        
        if includeHeaders is True:
            sb.write(header1 + "\n")
            sb.write(header2 + "\n")


        for i in range(len(lst)): 
            
            item = io.StringIO()    # string builder for items in a line  

            item.write(str(lst[i].ReportPeriod) + "\t")
            item.write(str(lst[i].PeriodNbr) + "\t")
            item.write(str(lst[i].ReportPeriodStart) + "\t")
            item.write(str(lst[i].ReportPeriodEnd) + "\t")
            item.write(str(lst[i].Server) + "\t")
            item.write(str(lst[i].Assignment) + "\t")
            item.write(str(lst[i].PerpetualLicense) + "\t")
            item.write(str(lst[i].Support) + "\t")
            item.write(str(lst[i].Subscription) + "\t")
            item.write(str(lst[i].SoftwareTotal) + "\t")
            item.write(str(lst[i].Power) + "\t")
            item.write(str(lst[i].Facility) + "\t")
            item.write(str(lst[i].Total) + "\t")
            
            sb.write(item.getvalue() + "\n")                
            
        return sb.getvalue()
    
    @classmethod
    def HardwareInventory(cls, includeHeaders:bool = True):

        lst = cls._forecast.HardwareInventory  

        if lst is None or len(lst) == 0:
            return str()      
        
        sb = io.StringIO()      # string builder for individual lines

        if hasattr(lst[0].RackQtyStart, 'property' ):
            header1 = "Report Period \t \t \t \t Rack Qty \t \t Server Qty \t \t Processor Qty \t \t Core Qty"
            header2 = "Month \t Nbr \t Start \t End \t Start \t End \t Start \t End \t Start \t End \t Start \t End"
        else:
            header1 = "Report Period \t \t \t \t Server Qty \t \t Processor Qty \t \t Core Qty"
            header2 = "Month \t Nbr \t Start \t End \t Start \t End \t Start \t End \t Start \t End"   


        header1 = header1.replace("  ", " ")
        header2 = header2.replace("  ", " ")
        
        if includeHeaders is True:
            sb.write(header1 + "\n")
            sb.write(header2 + "\n")


        for i in range(len(lst)): 
            
            item = io.StringIO()    # string builder for items in a line  

            item.write(str(lst[i].ReportPeriod) + "\t")
            item.write(str(lst[i].PeriodNbr) + "\t")
            item.write(str(lst[i].ReportPeriodStart) + "\t")
            item.write(str(lst[i].ReportPeriodEnd) + "\t")
            if hasattr(lst[i].RackQtyStart, 'property' ):
                item.write(str(lst[i].RackQtyStart) + "\t")
                item.write(str(lst[i].RackqtyEnd) + "\t")
            
            item.write(str(lst[i].ServerQtyStart) + "\t")
            item.write(str(lst[i].ServerQtyEnd) + "\t")
            item.write(str(lst[i].ProcessorQtyStart) + "\t")
            item.write(str(lst[i].ProcessorQtyEnd) + "\t")
            item.write(str(lst[i].CoreQtyStart) + "\t")
            item.write(str(lst[i].CoreQtyEnd) + "\t")
            
            sb.write(item.getvalue() + "\n")                
            
        return sb.getvalue()
    

    @classmethod
    def HardwareTransactions(cls, includeHeaders:bool = True):

        lst = cls._forecast.HardwareTransactions  

        if lst is None or len(lst) == 0:
            return str()      
        
        sb = io.StringIO()      # string builder for individual lines

        if hasattr(lst[0].RackQtyAdds, 'property' ):
            header1 = "Report Period \t \t \t \t Rack Qty \t \t Server Qty \t \t Processor Qty \t \t Core Qty"
            header2 = "Month \t Nbr \t Start \t End \t Adds \t Removals \t Adds \t Removals \t Adds \t Removals \t Add \t Removals"   

        else:
            header1 = "Report Period \t \t \t \t Server Qty \t \t Processor Qty \t \t Core Qty"
            header2 = "Month \t Nbr \t Start \t End \t Adds \t Removals \t Adds \t Removals \t Add \t Removals"     

        header1 = header1.replace("  ", "")
        header2 = header2.replace("  ", "")
        
        if includeHeaders is True:
            sb.write(header1 + "\n")
            sb.write(header2 + "\n")


        for i in range(len(lst)): 
            
            item = io.StringIO()    # string builder for items in a line  

            item.write(str(lst[i].ReportPeriod) + "\t")
            item.write(str(lst[i].PeriodNbr) + "\t")
            item.write(str(lst[i].ReportPeriodStart) + "\t")
            item.write(str(lst[i].ReportPeriodEnd) + "\t")
            if hasattr(lst[0].RackQtyAdds, 'property' ):
                item.write(str(lst[i].RackQtyAdds) + "\t")
                item.write(str(lst[i].RackqtyRemovals) + "\t")
            
            item.write(str(lst[i].ServerQtyAdds) + "\t")
            item.write(str(lst[i].ServerQtyRemovals) + "\t")
            item.write(str(lst[i].ProcessorQtyAdds) + "\t")
            item.write(str(lst[i].ProcessorQtyRemovals) + "\t")
            item.write(str(lst[i].CoreQtyAdds) + "\t")
            item.write(str(lst[i].CoreQtyRemovals) + "\t")
            
            sb.write(item.getvalue() + "\n")                
            
        return sb.getvalue()
    

    @classmethod
    def SoftwareInventory(cls, includeHeaders:bool = True):

        lst = cls._forecast.SoftwareInventory  

        if lst is None or len(lst) == 0:
            return str()      
        
        sb = io.StringIO()      # string builder for individual lines

        header1 = "Report Period \t \t \t \t License \t \t Contract \t Required \t \t Available \t \t Excess"
        header2 = "Month \t Nbr \t Start \t End \t Id \t Type \t Type \t Start \t End \t Start \t End \t Start \t End"
        
        header1 = header1.replace("  ", " ")
        header2 = header2.replace("  ", " ")
        
        if includeHeaders is True:
            sb.write(header1 + "\n")
            sb.write(header2 + "\n")


        for i in range(len(lst)): 
            
            for stack in lst[i].Stack:
                
                item = io.StringIO()    # string builder for items in a line  
                item.write(str(lst[i].ReportPeriod) + "\t")
                item.write(str(lst[i].PeriodNbr) + "\t")
                item.write(str(lst[i].ReportPeriodStart) + "\t")
                item.write(str(lst[i].ReportPeriodEnd) + "\t")
            
                # stack detail
                item.write(str(stack.LicenseId) + "\t")
                item.write(str(stack.LicenseType) + "\t")
                item.write(str(stack.ContractType) + "\t")
                item.write(str(stack.RequiredQtyStart) + "\t")
                item.write(str(stack.RequiredQtyEnd) + "\t")
                item.write(str(stack.AvailableQtyStart) + "\t")
                item.write(str(stack.AvailableQtyEnd) + "\t")
                item.write(str(stack.ExcessQtyStart) + "\t")
                item.write(str(stack.ExcessQtyEnd) + "\t")
            
                sb.write(item.getvalue() + "\n")                
            
        return sb.getvalue()
    

    @classmethod
    def FacilityResources(cls, includeHeaders:bool = True):

        lst = cls._forecast.FacilityResources  

        if lst is None or len(lst) == 0:
            return str()      
        
        sb = io.StringIO()      # string builder for individual lines

        header1 = "Report Period \t \t \t \t Rack Unit Qty (1U)"
        header2 = "Month \t Nbr \t Start \t End \t Start \t End \t KwHrs"
        
        header1 = header1.replace("  ", " ")
        header2 = header2.replace("  ", " ")
        
        if includeHeaders is True:
            sb.write(header1 + "\n")
            sb.write(header2 + "\n")


        for i in range(len(lst)): 
            
            item = io.StringIO()    # string builder for items in a line  

            item.write(str(lst[i].ReportPeriod) + "\t")
            item.write(str(lst[i].PeriodNbr) + "\t")
            item.write(str(lst[i].ReportPeriodStart) + "\t")
            item.write(str(lst[i].ReportPeriodEnd) + "\t")
            item.write(str(lst[i].RackUnitSlotQtyStart) + "\t")
            item.write(str(lst[i].RackUnitSlotQtyEnd) + "\t")
            item.write(str(lst[i].KilowattHrs) + "\t")
            
            sb.write(item.getvalue() + "\n")                
            
        return sb.getvalue()
    
    RackUnitSlotQtyStart: int
    RackUnitSlotQtyEnd: int
    KilowattHrs: int