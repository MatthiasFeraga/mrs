/* global fetch, FormData */

class FileSelect {
  // putUrl (string): file upload url
  // csrftoken (string): csrf token
  // el (dom element object): file input element to add msgs to
  // errorClass (string): error div classname
  constructor (putUrl, csrftoken, el, errorClass='error') {
    this.errorMsg = {
      mimeType: 'Mime type not valid',
      fileSize: 'File too large',
    }
    this.validMimeTypes = [
      'image/jpeg'
    ]
    this.maxFileSize = Math.pow(10, 7) // 10 MB
    this.putUrl = putUrl
    this.csrfToken = csrftoken
    this.el = el
    this.errorClass = errorClass
    this.hideErrorClassName = 'hidden'
  }

  //// validate file MIME type
  //// private, tested through this.validateFile
  // mimeType (string): file mime type
  mimeTypeValidate (mimeType) {
    return this.validMimeTypes.indexOf(mimeType) >= 0
  }

  //// Validate file size
  //// private, tested through this.validateFile
  // size (int): file size (bytes)
  fileSizeValidate (size) {
    return size <= this.maxFileSize
  }

  //// Upload file validation
  // file (file object): upload file object
  isFileValid (file) {
    if (!this.mimeTypeValidate(file.type)) {
      this.error(this.errorMsg.mimeType)
      return false
    }

    if (!this.fileSizeValidate(file.size)) {
      this.error(this.errorMsg.fileSize)
      return false
    }

    return true
  }

  //// make upload file request
  // file (file object): file to upload
  async putRequest (file) {
    const data = new FormData()
    data.append('file', file)

    const headers = {
      'X-CSRFToken': this.csrfToken,
      'content-type': ''
    }

    const putOptions = {
      method: 'POST',
      headers,
      body: data
    }

    return await fetch(this.putUrl, putOptions)
  }

  //// Send delete file request
  // deleteUrl (string): delete url for file
  async deleteRequest (deleteUrl) {
    const deleteOptions = {
      method: 'DELETE'
    }

    try {
      await fetch(deleteUrl, deleteOptions)

      this.deleteSuccess(deleteUrl)
    } catch (e) {
      this.error(e)
    }
  }

  //// Upload file
  // file = file object
  async upload (file) {
    // request
    if (this.isFileValid(file)) {
      try {
        const resp = await this.putRequest()

        this.success(file, resp)
      } catch (e) {
        this.error(e)
      }
    }
  }

  //// delete file success
  // deleteUrl (string): url endpoint to delete file
  deleteSuccess(deleteUrl) {
    const filesElement = this.getFilesElement()
    const elToRemove = filesElement.querySelector('a[href="' + deleteUrl + '"]')

    elToRemove.parentNode.parentNode.removeChild(elToRemove.parentNode)
  }

  //// upload file success
  // file = file object
  // response = ajax response
  success (file, response) {
    const ul = this.getFilesElement()
    ul.innerHTML += (
      '<li>'
      + '<span>'
      + file.name
      + '</span>'
      + '<a href="' + response.deleteUrl + '">'
      + 'remove'
      + '</a>'
      + '</li>'
    )

    // formatting ul.innerHTML as 1 liner
    var i = ul.innerHTML.indexOf('<');
    ul.innerHTML = ul.innerHTML.substr(i, ul.innerHTML.length - 1)
  }

  //// upload file error
  // error (object): error exception
  error(error) {
    const errorMsg = error
    this.updateErrorMsg(errorMsg)
    this.showError()
  }

  //// Returns DOM element containing error msg
  getErrorElement() {
    return this.el.querySelector('.' + this.errorClass)
  }

  //// Returns DOM element containing files list
  getFilesElement() {
    return this.el.querySelector('ul')
  }

  //// updates error field
  // errorMsg (strin): error message
  updateErrorMsg(errorMsg) {
    const errorElement = this.getErrorElement()
    errorElement.innerHTML = errorMsg
  }

  //// shows error message
  showError() {
    const errorElement = this.getErrorElement()
    errorElement.classList.remove(this.hideErrorClassName)
  }

  //// hides error message
  hideError() {
    const errorElement = this.getErrorElement()
    errorElement.classList.add(this.hideErrorClassName)
  }
}

module.exports = FileSelect