

// pdf coordinates

searchname = [0, 190, 360, 345 ];
searchapplicant = [0, 335, 360, 510 ];
searchfee = [0, 0, 360, 155 ];
searchtop = [0, 0, 360, 155 ];

  jQuery(function($){

    // The variable jcrop_api will hold a reference to the
    // Jcrop API once Jcrop is instantiated.
    var jcrop_api;
    
    // In this example, since Jcrop may be attached or detached
    // at the whim of the user, I've wrapped the call into a function
    initJcrop();
    
    // The function is pretty simple
    function initJcrop()//{{{
    {
      // Hide any interface elements that require Jcrop
      // (This is for the local user interface portion.)
      $('.requiresjcrop').hide();

      // Invoke Jcrop in typical fashion
      $('#target').Jcrop({
        onChange: showPreview
      },function(){

        jcrop_api = this;
        jcrop_api.animateTo(searchtop);

        // Setup and dipslay the interface for "enabled"
        $('#can_click,#can_move,#can_size').attr('checked','checked');
        $('#ar_lock,#size_lock,#bg_swap').attr('checked',false);
        $('.requiresjcrop').show();

      });

    };
    //}}}
	var $preview = $('#preview');
	function showPreview(coords){
		var rx = 100 / coords.w;
		var ry = 290 / coords.h;
		
		$('#preview').css({
			width: Math.round(rx * 2700) + 'px',
			height: Math.round(ry * 490) + 'px',
			marginLeft: '-' + Math.round(rx * coords.x) + 'px',
			marginTop: '-' + Math.round(ry * coords.y) + 'px'
		});
	
	}

      $('#searchapplicant').click(function(e) {
      // Sets a random selection
      jcrop_api.animateTo(searchapplicant)
    });
      $('#searchname').click(function(e) {
      // Sets a random selection
      jcrop_api.animateTo(searchname);
    });
     $('#searchfee').click(function(e) {
      // Sets a random selection
      jcrop_api.animateTo(searchfee)
    });
   
  });




