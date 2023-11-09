(() => {
  'use strict'
  const open_dialog = document.getElementById('open_dialog')
  open_dialog.style.display = 'none'

  const date_form = document.getElementById('id_date_form')
  const modal_form = document.getElementById('id_modal_form')

  date_form.addEventListener('submit', event => {
    event.preventDefault()
    event.stopPropagation()
    date_form.classList.add('was-validated')

    if (date_form.checkValidity()) {
      const date_form_data = new FormData(date_form)
      fetch('', {
        method: 'POST',
        body: date_form_data
      })
      open_dialog.click()

    }
  }, false)


  modal_form.addEventListener('submit', event => {
    if (!modal_form.checkValidity()) {
      event.preventDefault()
      event.stopPropagation()
    }

    modal_form.classList.add('was-validated')
  }, false)

})()