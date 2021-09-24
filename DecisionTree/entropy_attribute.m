function stuff = entropy_attribute(data,attributes_aval)
    
    global depth;
    
    for i=1:length(attributes_aval)
        if(attributes_aval(i) == "-1")
            stuff(i) = 0;
            continue
        else 
            stuff(i) = entropy_att_aval(attributes_aval(i),data);
        end 
    end 
        
end 