/*function GetAvitoId(url) {
            var id = url.match (/[^\?]*_(\d+)($|#.*|\?.*)/);
//          console.log ("Url "+url);
//          console.log (id);
            if (!id)
                return "";
            return "avito:"+id[1];
        };
		
*/
document.addEventListener('DOMContentLoaded', function() {
	var checkPageButton = document.getElementById('checkPage');
	checkPageButton.addEventListener('click', function() {

	var message = document.getElementById('message').value;
	var author = document.getElementById('author').value;
	
	
	/*var xxx = chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT},
		function(tabs){
		return(tabs[0].url);
   });*/
   //alert(xxx);
	
	var data = 
	{
	"id_item": "1234", 
	"message": message, 
	"author": author
	};
	
	$.ajax({
		type : "POST",
		url : "http://localhost:5000/comment/",
		data: JSON.stringify(data, null, '\t'),
		contentType: 'application/json;charset=UTF-8',
		success: function(result) {
			//window.alert(result);
		}
	});		
  
    window.alert("Ended")
  }, false);
}, false);