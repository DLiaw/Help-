import React, { useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { getAllReviews } from '../../store/review'
import SingleReview from './SingleBusiness'
import './landingPage.css'

// Landing page components

const LandingPage = () => {
    const allReview = useSelector(state => Object.values(state.review.allReviews))

    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(getAllReviews())
    }, [dispatch])

    return (
        <div>
            {allReview.map(review => (
                <SingleReview key={review.id} review={review} />
            ))}
        </div>
    )
}


export default LandingPage;
