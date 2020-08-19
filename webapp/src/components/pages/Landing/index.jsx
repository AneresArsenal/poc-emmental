import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { requestData } from 'redux-thunk-data'

import Header from 'components/layout/Header'
import Main from 'components/layout/Main'

import VerdictItem from './VerdictItem'


const KEYWORDS_CHAIN = 'coronavirus'


export default () => {
  const dispatch = useDispatch()

  const verdicts = useSelector(state => state.data.verdicts)


  useEffect(() => {
    const apiPath = `/verdicts?keywords=${KEYWORDS_CHAIN}`
    dispatch(requestData({ apiPath }))
  }, [dispatch])


  return (
    <>
      <Header />
      <Main className="landing">
        <div className="container">
          <section className="title">
            {`verdicts for "${KEYWORDS_CHAIN}": `}
          </section>
          <section className="results">
            {(verdicts || []).map(verdict => (
              <VerdictItem 
                key={verdict.id}
                verdict={verdict}
              />
            ))}
          </section>
        </div>
      </Main>
    </>
  )
}
