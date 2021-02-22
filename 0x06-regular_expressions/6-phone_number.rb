#!/usr/bin/env ruby
# Ruby script that takes argument and pass it to a matching method
puts ARGV[0].scan(/^\d[415][0-9]{7}\d$/).join
