import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { deleteOldBusiness, cleanupBusiness } from "../../store/business";
import { NavLink, useHistory } from "react-router-dom";
import './businessDetail.css'
import Stars from "../stars";

const SingleBusiness = ({ business }) => {

    const dispatch = useDispatch()
    const user = useSelector(state => state.session.user)
    const history = useHistory()
    const handleSubmit = async (e) => {
        e.preventDefault()
        dispatch(deleteOldBusiness(business.id))
        dispatch(cleanupBusiness())
        history.push('/')
        history.go(0)
    }

    let rating = 0;
    business.reviews?.forEach(e => {
        rating += e.stars
    })
    rating = rating / business.reviews.length

    return (
        <div>
            <div className="business-name-info">
                <h3>
                    {business.name}
                </h3>

                <div>
                    <div style={{ width: '100px' }}>
                        <Stars rating={rating} />
                    </div>
                    {business.reviews?.length} Reviews
                </div>
                <div>
                    {business.price} • {business.business_type}
                </div>
                <div className="hours-edit-delete">
                    {business.monOpen}-{business.monClose}&nbsp;&nbsp;&nbsp;&nbsp;
                    {user?.id == business.owner_id && user && <div>
                        <button className="edit-delete-button" onClick={handleSubmit}>Delete</button>&nbsp;&nbsp;
                        <NavLink to={`/business/${business.id}/edit`}><button className="edit-delete-button" >Edit</button></NavLink>
                    </div>}
                </div>
            </div>
        </div >
    )
}

export default SingleBusiness;
