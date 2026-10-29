vehicle = {
&quot;class&quot;: &quot;Vehicle&quot;,
&quot;brand&quot;: &quot;Toyota&quot;,
&quot;fuel_type&quot;: &quot;Petrol&quot;,
&quot;wheels&quot;: 4,
&quot;color&quot;: &quot;White&quot;
}
print(&quot;Vehicle Frame&quot;)
for slot, value in vehicle.items():
print(slot, &quot;:&quot;, value)
