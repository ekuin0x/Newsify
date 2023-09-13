(async()=>{
    const q = $("#q").attr("name")
    url = `/related/${q}`
    const res2 = await fetch(url)
    const related = await res2.text()
   $("#related").html(related)
   
})()

$(document).ready(()=>{
    $("form").attr("action", "javascript:void(0);")
    $("button").attr("type", "submit") 
})
