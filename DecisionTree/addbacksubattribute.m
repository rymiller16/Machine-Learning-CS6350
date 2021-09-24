function sub_attributes = addbacksubattribute(node_string,sub_attributes)
    if node_string == "buying"
        sub_attributes(1:4,1) = ["vhigh"; "high"; "med"; "low"];
    elseif node_string == "maint"
        sub_attributes(1:4,2) = ["vhigh"; "high"; "med"; "low"];
    elseif node_string == "doors"
        sub_attributes(1:4,3) = ["2"; "3"; "4"; "more"];
    elseif node_string == "persons"
        sub_attributes(1:4,4) = ["2"; "3"; "more";"-1"];
    elseif node_string == "lug_boot"
        sub_attributes(1:4,5) = ["small"; "med"; "big";"-1"];
    elseif node_string == "safety"
        sub_attributes(1:4,6) = ["low"; "med"; "high";"-1"];
    end
end