$(function() {
    $(document).on('keyup', 'input[id^="id_form-"]', function() {
        input_val = $(this).val();
        console.log(input_val);
        if (input_val != '') {
            $(".form-name").html("formulaire de "+input_val);
        } else {
            $(".form-name").html("formulaire");
        }
    });

    /*$('input#id_form-0-nom_et_prenom').on('keyup', function(){
        input_val = $('input#id_form-0-nom_et_prenom').val();
        if (input_val != '') {
            $(".form-name").html("formulaire de "+input_val);
        } else {
            $(".form-name").html("formulaire");
        }
    })*/

    //==========================rechercher bar================
    $('#empty-result').html('');
    $('#query').keyup(function(){
        var input = $(this).val();
        query = {
            name:$(this).attr('name'),
            value:$(this).val()
        }
        if(input.length>0){
            $.ajax({
                url: $(this).attr("data-url"),
                type:'get',
                dataType:'json',
                data: query,
                beforeSend:function(){
                    $('#spinner').addClass('active');
                },
                success:function(data){
                    $('#spinner').removeClass('active');
                    $('#person-evang tbody').html(data.models);
                    console.log(data.models)
                    $('#result-search').html(data.counter_str);
                    if (data.counter == 0) {
                        $('#empty-result').html(data.empty_result);
                    } else {
                        $('#empty-result').html('');
                    }
                }
            });
        }else{
            $.ajax({
                url: $(this).attr("data-url"),
                type:'get',
                dataType:'json',
                beforeSend:function(){
                    $('#spinner').addClass('active');
                },
                success:function(data){
                    $('#spinner').removeClass('active');
                    $('#person-evang tbody').html(data.models);
                    $('#result-search').html("");
                }
            })
        }
        
    })
});