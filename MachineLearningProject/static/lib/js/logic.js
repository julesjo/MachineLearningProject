var SelectText="{{ SelectText }}"

d3.select("#btn-success").on('click',function () {

//collectValues()
myOnChange();
});


function myOnChange(){
alert("Hi")
d3.select('#SelectText').html("SelectText")
// audio = d3.select("#audodiv").append("audio")
//           .attr("src","{% say 'en-us' '{{ ScreenText }}' %}")
//           .attr("controls")
}
