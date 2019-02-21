$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    var formb = $('#full_form');
    console.log('Modifying Details');
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      data: formb.serialize(),
      dataType: 'json',
      beforeSend: function () {
        $("#modal-strategy .modal-content").html("");
        $("#modal-strategy").modal("show");
      },
      success: function (data) {
        $("#modal-strategy .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    console.log('Details Modified');
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#modal-strategy").modal("hide");
          if (typeof(Storage) !== "undefined") {
            // https://stackoverflow.com/q/6193574/5176549
            sessionStorage.setItem("strategy_details", JSON.stringify(data.strategy_details));
          }
        }
        else {
          $("#modal-strategy .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  var saveBacktest = function () {
    var strategy_details = $('#id_strategy_details');

    if (sessionStorage.length == 0){
      sessionStorage.setItem('strategy_details','null');
      var data=sessionStorage.getItem('strategy_details');
      console.log('Still not data passed');
    }
    else {
      var data=sessionStorage.getItem('strategy_details');
      console.log('Backtest details loaded' + data);
    }
    $('#id_strategy_details').val(data);
  };


  var resetDetails = function () {
    sessionStorage.setItem('strategy_details','null');
    data=sessionStorage.getItem('strategy_details');
    console.log('Details reset');
    $('#id_strategy_details').val(data);
  };




  // Modify strategy
  $(".js-modify-strategy-details").click(loadForm);
  $("#modal-strategy").on("submit", ".js-strategy-create-form", saveForm);



  //Modification of the strategy_details
  // https://stackoverflow.com/questions/44087655/edit-form-field-value-on-template
  $(".js-create-backtest").click(saveBacktest);
  $(".js-reset-details").change(resetDetails);

});
