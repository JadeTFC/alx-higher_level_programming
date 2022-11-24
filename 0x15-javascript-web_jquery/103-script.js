const $ = window.$;

$(document).ready(function () {
  function fetchTranslation () {
    const lang = $('input#language_code').val();
    $.get(`https://stefanbohacek.com/hellosalut/?lang=${lang}`, data => {
      $('div#hello').text(data.hello);
    });
  }
  $('input#btn_translate').click(fetchTranslation);
  $('input#language_code').keypress((e) => {
    if (e.key === 'Enter') {
      fetchTranslation();
    }
  });
});
