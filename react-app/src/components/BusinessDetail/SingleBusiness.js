import React from "react";

const SingleBusiness = ({ business }) => {
    return (
        <div>
            <div>
                <h3>
                    {business.name}
                </h3>
                <div>
                    {business.reviews?.length} Reviews
                </div>
                <div>
                    {business.price} • {business.business_type}
                </div>
                <div>
                    {business.monOpen}{business.monClose}
                </div>
            </div>
            <div>
                {/* <div>
                    <a href={business.site}>{business.site}</a>
                </div> */}
            </div>
        </div >
    )
}

export default SingleBusiness;
