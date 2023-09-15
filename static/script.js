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
    $("button").attr("onclick", "search()") 
})

const search = async ()=>{
    let q = $("input[type='search']").val()
    let res = await fetch("/search/" + q)
    let html = await res.text()
    $("#wrapper").html(html)
}
