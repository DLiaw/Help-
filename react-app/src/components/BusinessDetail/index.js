import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams, NavLink } from 'react-router-dom';
import { getOneBusiness } from '../../store/business';
import SingleBusiness from './SingleBusiness'
import BusinessReviews from './BusinessReviews'
import Navbar from './Nav.js'
import './businessDetail.css'
// Business details page

const BusinessDetail = () => {
    const [load, setLoad] = useState(false)
    const business = useSelector(state => state.business?.oneBusiness)
    const { id } = useParams();
    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(getOneBusiness(id)).then(() => setLoad(true))
    }, [dispatch])
    if (!Object.values(business).length) return null;
    return load && (

        <div className='business-outer'>
            <Navbar business={business} />
            <div className='business-images'>
                <div className='business-gradient'></div>
                <div className='business-solo-image'>
                    {business.images?.map(e => (
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
            <div className='review-business-info'>
                <div className='user-reviews'>
                    {business.reviews?.map(singleReview => (
                        <BusinessReviews key={singleReview.id} singleReview={singleReview} />
                    ))}
                </div>
                <div className='business-info'>
                    <div>
                        <NavLink to={business.site} className='business-info-site'>
                            {business.site}<i class="fa-solid fa-location-arrow" />
                        </NavLink>
                    </div>
                    <div className='business-info-phone'>
                        {business.phone_number}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        &nbsp;<i class="fa-solid fa-phone-volume" />
                    </div>
                    <div className='business-info-address'>
                        <div className='business-info-address-detail'>
                            {business.address}.&nbsp;{business.city}&nbsp;
                            {business.state},&nbsp;{business.zip}
                        </div>
                        <div>
                            <i class="fa-solid fa-location-dot" />
                        </div>
                    </div>
                </div>
            </div>
        </div>

    )

}

export default BusinessDetail;
