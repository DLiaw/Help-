import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useHistory, useParams } from 'react-router-dom';
import { updateBusiness } from '../../store/business';
import image1 from './image1.png'
import image2 from './image2.png'
import './EditBusiness.css'


const hours = [
    '12:00 AM', '12:30 AM', '1:00 AM', '1:30 AM', '2:00 AM', '2:30 AM',
    '3:00 AM', '3:30 AM', '4:00 AM', '4:30 AM', '5:00 AM', '5:30 AM',
    '6:00 AM', '6:30 AM', '7:00 AM', '7:30 AM', '8:00 AM', '8:30 AM',
    '9:00 AM', '9:30 AM', '10:00 AM', '10:30 AM', '11:00 AM', '11:30 AM',
    '12:00 PM', '12:30 PM', '1:00 PM', '1:30 PM', '2:00 PM', '2:30 PM',
    '3:00 PM', '3:30 PM', '4:00 PM', '4:30 PM', '5:00 PM', '5:30 PM',
    '6:00 PM', '6:30 PM', '7:00 PM', '7:30 PM', '8:00 PM', '8:30 PM',
    '9:00 PM', '9:30 PM', '10:00 PM', '10:30 PM', '11:00 PM', '11:30 PM', 'Closed']
const states = [
    'AK', 'AL', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE',
    'FL', 'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY',
    'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MP', 'MS', 'MT',
    'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK',
    'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UM', 'UT',
    'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY']

const priceOption = ['$', '$$', '$$$', '$$$$']


const EditBusinessForm = () => {
    const user = useSelector(state => state.session.user)
    const dispatch = useDispatch()
    const history = useHistory()
    const [errors, setErrors] = useState({})
    const [name, setName] = useState('')
    const [address, setAddress] = useState('')
    const [city, setCity] = useState('')
    const [state, setState] = useState('')
    const [zip, setZip] = useState('')
    const [price, setPrice] = useState('')
    const [phone_number, setPhone] = useState('')
    const [business_type, setType] = useState('')
    const [monOpen, setMon] = useState('')
    const [tueOpen, setTue] = useState('')
    const [wedOpen, setWed] = useState('')
    const [thuOpen, setThu] = useState('')
    const [friOpen, setFri] = useState('')
    const [satOpen, setSat] = useState('')
    const [sunOpen, setSun] = useState('')
    const [monClose, setMonClose] = useState('')
    const [tueClose, setTueClose] = useState('')
    const [wedClose, setWedClose] = useState('')
    const [thuClose, setThuClose] = useState('')
    const [friClose, setFriClose] = useState('')
    const [satClose, setSatClose] = useState('')
    const [sunClose, setSunClose] = useState('')
    const [site, setSite] = useState('')
    const [time, setTime] = useState(false)
    const { id } = useParams()

    const handleSubmit = async (e) => {
        e.preventDefault()
        const data = {
            name, address, city, state, zip, price, phone_number, business_type,
            monOpen, tueOpen, wedOpen, thuOpen, friOpen, satOpen, sunOpen, monClose,
            tueClose, wedClose, thuClose, friClose, satClose, sunClose, site,
            owner_id: user.id.toString(), id
        }
        const business = await dispatch(updateBusiness(data))
        for (let key in business.errors) {
            if (key === 'monOpen' || key === 'tueOpen' || key === ' wedOpen' || key === ' thuOpen' || key === ' friOpen' || key === ' satOpen' || key === ' sunOpen' || key === 'monClose' ||
                key === 'tueClose' || key === 'wedClose' || key === 'thuClose' || key === 'friClose' || key === 'satClose' || key === 'sunClose') {
                setTime(true)
            }

        }
        if (business.errors) {
            setErrors(business.errors);
        } else {
            history.push(`/business/${id}`)
        }
    }

    return (
        <div className='form-main-div'>
            <div>
                <h3 style={{ color: 'rgba(211, 35, 35, 255)' }}>Provide Business details.</h3>
                <label style={{ color: 'red' }}>* fields are required.</label>
                <form className='business-form' onSubmit={handleSubmit}>
                    <div className='single-form-div'>
                        <label id='ptag'>Business name*</label>
                        <input className='input-field' type="text"
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                            placeholder="Business name"
                        ></input>
                        {errors.name && (
                            <div className='errors'>{errors.name}</div>
                        )}
                    </div>
                    <div className='single-form-div'>
                        <label id='ptag'>Address*</label>
                        <input className='input-field' type="text"
                            value={address}
                            onChange={(e) => setAddress(e.target.value)}
                            placeholder="Address"
                        ></input>
                        {errors.address && (
                            <div className='errors'>{errors.address}</div>
                        )}
                    </div>
                    <div className='single-form-div'>
                        <label id='ptag'>City*</label>
                        <input className='input-field' type="text"
                            value={city}
                            onChange={(e) => setCity(e.target.value)}
                            placeholder="City"
                        ></input>
                        {errors.city && (
                            <div className='errors'>{errors.city}</div>
                        )}
                    </div>
                    <div className='single-form-div'>
                        <label id='ptag'>State*</label>
                        <select className='state-price' type="text"
                            value={state}
                            onChange={(e) => setState(e.target.value)}>
                            <option value="" disabled defaultValue hidded="true">State</option>{states.map((state, i) => (<option key={i} value={state}>{state}</option>))}
                        </select>
                        {errors.state && (
                            <div className='errors'>{errors.state}</div>
                        )}
                    </div>
                    <div className='single-form-div'>
                        <label id='ptag'>Zip code*</label>
                        <input className='input-field' type="text"
                            value={zip}
                            onChange={(e) => setZip(e.target.value)}
                            placeholder="Zip code"
                        ></input>
                        {errors.zip && (
                            <div className='errors'>{errors.zip}</div>
                        )}
                    </div>
                    <div className='single-form-div'>
                        <label id='ptag'>Pirce*</label>
                        <select className='state-price' type="text"
                            value={price}
                            onChange={(e) => setPrice(e.target.value)}>
                            <option value="" disabled defaultValue hidded="true">Price</option>{priceOption.map((price, i) => (<option key={i} value={price}>{price}</option>))}
                        </select>
                        {errors.price && (
                            <div className='errors'>{errors.price}</div>
                        )}
                    </div>
                    <div className='single-form-div'>
                        <label id='ptag'>Phone number*</label>
                        <input className='input-field' type="text"
                            value={phone_number}
                            onChange={(e) => setPhone(e.target.value)}
                            placeholder="Phone number"
                        ></input>
                        {errors.phone_number && (
                            <div className='errors'>{errors.phone_number}</div>
                        )}
                    </div>
                    <div className='single-form-div'>
                        <label id='ptag'>Business type*</label>
                        <input className='input-field' type="text"
                            value={business_type}
                            onChange={(e) => setType(e.target.value)}
                            placeholder="Business type"
                        ></input>
                        {errors.business_type && (
                            <div className='errors'>{errors.business_type}</div>
                        )}
                    </div>
                    <label id='ptag'>Business Hours*</label>
                    <div className='hours'>
                        <div id='days'>Mon</div>
                        <div className='hours2'>
                            <select type="text"
                                required
                                value={monOpen}
                                onChange={(e) => setMon(e.target.value)}>
                                <option value="" disabled defaultValue hidded="true">Open</option>{hours.map((hour, i) => (<option key={i} value={hour}>{hour}</option>))}
                            </select>
                            <select type="text"
                                required
                                id='close-select'
                                value={monClose}
                                onChange={(e) => setMonClose(e.target.value)}>
                                <option value="" disabled defaultValue hidded="true">Close</option>{hours.map((hour, i) => (<option key={i} value={hour}>{hour}</option>))}
                            </select>
                        </div>
                    </div>
                    <div className='hours'>
                        <div id='days'>Tue</div>
                        <div className='hours2'>
                            <select type="text"
                                required
                                value={tueOpen}
                                onChange={(e) => setTue(e.target.value)}>
                                <option value="" disabled defaultValue hidded="true">Open</option>{hours.map((hour, i) => (<option key={i} value={hour}>{hour}</option>))}
                            </select>
                            <select type="text"
                                required
                                id='close-select'
                                value={tueClose}
                                onChange={(e) => setTueClose(e.target.value)}>
                                <option value="" disabled defaultValue hidded="true">Close</option>{hours.map((hour, i) => (<option key={i} value={hour}>{hour}</option>))}
                            </select>
                        </div>
                    </div>
                    <div className='hours'>
                        <div id='days'>Wed</div>
                        <div className='hours2'>
                            <select type="text"
                                required
                                value={wedOpen}
                                onChange={(e) => setWed(e.target.value)}>
                                <option value="" disabled defaultValue hidded="true">Open</option>{hours.map((hour, i) => (<option key={i} value={hour}>{hour}</option>))}
                            </select>
                            <select type="text"
                                required
                                id='close-select'
                                value={wedClose}
                                onChange={(e) => setWedClose(e.target.value)}>
                                <option value="" disabled defaultValue hidded="true">Close</option>{hours.map((hour, i) => (<option key={i} value={hour}>{hour}</option>))}
                            </select>
                        </div>
                    </div>
                    <div className='hours'>
                        <div id='days'>Thu</div>
                        <div className='hours2'>
                            <select type="text"
                                required
                                value={thuOpen}
                                onChange={(e) => setThu(e.target.value)}>
                                <option value="" disabled defaultValue hidded="true">Open</option>{hours.map((hour, i) => (<option key={i} value={hour}>{hour}</option>))}
                            </select>
                            <select type="text"
                                required
                                id='close-select'
                                value={thuClose}
                                onChange={(e) => setThuClose(e.target.value)}>
                                <option value="" disabled defaultValue hidded="true">Close</option>{hours.map((hour, i) => (<option key={i} value={hour}>{hour}</option>))}
                            </select>
                        </div>
                    </div>
                    <div className='hours'>
                        <div id='days'>Fri</div>
                        <div className='hours2'>
                            <select type="text"
                                required
                                value={friOpen}
                                onChange={(e) => setFri(e.target.value)}>
                                <option value="" disabled defaultValue hidded="true">Open</option>{hours.map((hour, i) => (<option key={i} value={hour}>{hour}</option>))}
                            </select>
                            <select type="text"
                                required
                                id='close-select'
                                value={friClose}
                                onChange={(e) => setFriClose(e.target.value)}>
                                <option value="" disabled defaultValue hidded="true">Close</option>{hours.map((hour, i) => (<option key={i} value={hour}>{hour}</option>))}
                            </select>
                        </div>
                    </div>
                    <div className='hours'>
                        <div id='days'>Sat</div>
                        <div className='hours2'>
                            <select type="text"
                                required
                                value={satOpen}
                                onChange={(e) => setSat(e.target.value)}>
                                <option value="" disabled defaultValue hidded="true">Open</option>{hours.map((hour, i) => (<option key={i} value={hour}>{hour}</option>))}
                            </select>
                            <select type="text"
                                required
                                id='close-select'
                                value={satClose}
                                onChange={(e) => setSatClose(e.target.value)}>
                                <option value="" disabled defaultValue hidded="true">Close</option>{hours.map((hour, i) => (<option key={i} value={hour}>{hour}</option>))}
                            </select>
                        </div>
                    </div>
                    <div className='hours'>
                        <div id='days'>Sun</div>
                        <div className='hours2'>
                            <select type="text"
                                required
                                value={sunOpen}
                                onChange={(e) => setSun(e.target.value)}>
                                <option value="" disabled defaultValue hidded="true">Open</option>{hours.map((hour, i) => (<option key={i} value={hour}>{hour}</option>))}
                            </select>

                            <select type="text"
                                required
                                id='close-select'
                                value={sunClose}
                                onChange={(e) => setSunClose(e.target.value)}>
                                <option value="" disabled defaultValue hidded="true">Close</option>{hours.map((hour, i) => (<option key={i} value={hour}>{hour}</option>))}
                            </select>
                        </div>
                    </div>
                    {time && (
                        <div className='errors'>Please choose a time.</div>
                    )}
                    <div className='single-form-div'>
                        <label>Your website</label>
                        <input className='input-field' type="text"
                            value={site}
                            onChange={(e) => setSite(e.target.value)}
                            placeholder="Your site"
                        ></input>
                        {errors.site && (
                            <div className='errors'>{errors.site}</div>
                        )}
                    </div>
                    <div className='single-form-div'>
                        <div style={{ paddingTop: '10px' }}>
                            <button onClick={handleSubmit} className='create-business'>Update business</button>
                        </div>
                    </div>
                </form>
            </div>
            <div className='business-images-div'>
                <h2 id='text1' >Grow your business faster</h2>
                <div id='business-image1'>
                    <img id='business-image1' alt='image1' src={image1}></img>
                </div>
                <div className='image2-div'>
                    <img id='business-image2' alt='image2' src={image2}></img>
                    <h3 id='text2'>Reach more people who are ready to spend with help!</h3>
                </div>
            </div>
        </div>
    )

}


export default EditBusinessForm;
