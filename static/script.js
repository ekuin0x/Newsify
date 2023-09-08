(async()=>{
    const res0 = await fetch('/head')
    const head = await res0.text()
    $("head").append(head) 
    alert(head)

    const q = $("#q").attr("name")
    url = `/related/${q}`
    const res2 = await fetch(url)
    const related = await res2.text()
   $("#related").html(related)
})()

const search = async ()=>{
    let query = $("#query").val()
    let searchHtml = await fetch('/search/' + query )
    let res = await searchHtml.text()
    $("#wrapper").html(res)
}