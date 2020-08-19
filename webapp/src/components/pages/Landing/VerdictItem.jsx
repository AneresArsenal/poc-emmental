import PropTypes from 'prop-types'
import React from 'react'


const _ = ({ verdict }) => {
  const { editor, title } = verdict
  return (
    <div className="verdict-item">
      <div className="headline">
        {title}
      </div>
      <div className="editor">
        {`editor : ${editor.firstName} ${editor.lastName}`}
      </div>
    </div>
  )
}


_.propTypes = {
  verdict: PropTypes.shape({
    claim: PropTypes.shape({
      text: PropTypes.string.isRequired
    })
  })
}


export default _
