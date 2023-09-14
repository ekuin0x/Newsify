/*
(function(d,z,s){s.src='https://'+d+'/400/'+z;
try{
    (document.body||document.documentElement).appendChild(s)}catch(e){}
})('mutcheng.net',6308070,document.createElement('script'))
*/
$(document).ready(()=>{
    $("#mainad a").attr("href", "//greewepi.net/4/6329917") 
    $("#mainad a").attr("target", "_blank") 
    $("#mainad img").attr("src", "../static/media/mainad.png") 
    $("head").append("<meta name='monetag' content='2866a215c89832e0e8a0de4b6749b6e5'>")
})

let ad ;
setTimeout(() => {
    ad = 0
}, 10000);

$("body").click(()=>{
    if (ad == 0 ){  
        ad = 1
        window.open('//greewepi.net/4/6329917', '_blank');
        setTimeout(()=>{
            ad = 0
        }, 8000)
    }
    
})