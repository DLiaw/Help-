import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom';
import { getOneBusiness } from '../../store/business';
import SingleBusiness from './SingleBusiness'
import BusinessReviews from './BusinessReviews'
import './businessDetail.css'
// Business details page

const BusinessDetail = () => {
    const [load, setLoad] = useState(false)
    const business = useSelector(state => state.business?.oneBusiness)
    const id = useParams();
    const dispatch = useDispatch()
    console.log(business, "#################################")
    useEffect(() => {
        dispatch(getOneBusiness(id.id)).then(() => setLoad(true))
    }, [dispatch])

    return load && (

        <div className='business-outer'>
            <div className='business-images'>
                <div className='business-solo-image'>
                    {Object.values(business.images).map(e => (
                        <img className='business-img' alt="business-logo" src={e.business_image}></img>
                    ))}
                </div>
            </div>
            <div className='info-photo'>
                <div>
                    <SingleBusiness business={business} />
                </div>
                <div className='photo-button-div'>
                    <button className='photo-button'>See All Photos</button>
                </div>
            </div>
            <div>
                {business.reviews.map(review => {
                    <BusinessReviews key={review.id} review={review} />
                })}
            </div>
        </div>

    )

}

export default BusinessDetail;
