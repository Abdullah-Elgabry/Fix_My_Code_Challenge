###
#
#  this will re-order the args in asc order
#
###

lst_records = []
ARGV.each do |arg|
    next if arg !~ /^-?[0-9]+$/

    i_arg = arg.to_i
    
    is_inserted = false
    i = 0
    l = lst_records.size
    while !is_inserted && i < l do
        if lst_records[i] < i_arg
            i += 1
        else
            lst_records.insert(i, i_arg)
            is_inserted = true
            break
        end
    end
    lst_records << i_arg if !is_inserted
end

puts lst_records
