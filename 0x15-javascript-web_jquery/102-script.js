const $ = window.$;

$(document).ready(function () {
  $('input#btn_translate').click(function () {
    const lang = $('input#language_code').val();
    $.get(`https://stefanbohacek.com/hellosalut/?lang=${lang}`, data => {
      $('div#hello').text(data.hello);
    });
  });
});
