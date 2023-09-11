(async()=>{
    let head = 
    "<script async src='https://www.googletagmanager.com/gtag/js?id=G-KBVD10W104'></script><script>"+
    "window.dataLayer = window.dataLayer || [];function gtag(){dataLayer.push(arguments);}"+
    "gtag('js', new Date());gtag('config', 'G-KBVD10W104');</script>"
    $("head").prepend(head)
    //const res0 = await fetch('/head')
    //const head = await res0.text()
    //$("head").append(head) 

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

