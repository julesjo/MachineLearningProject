var micstatus="off"
var SelectText="{{ SelectText }}"

d3.select("#mymic").on('click',function () {

//collectValues()
myOnChange();
});


function myOnChange(){
alert(micstatus)
d3.select('#SelectText').html("SelectText")
if (micstatus=="off"){
d3.select('#mymic').attr('class', 'btn-transparent btn-recording')
.html('<i class="fas fa-microphone-alt fa-5x" style="color:white;">')
d3.select('.switchtext').text("Please talk now ... ")
micstatus='on'
}
else{
micstatus='off'
d3.select('#mymic').attr('class', 'btn-transparent')
.html('<i class="fas fa-microphone-alt-slash fa-5x" style="color:lightblue;">')
d3.select('.switchtext').text("Hi There!")
}
}
