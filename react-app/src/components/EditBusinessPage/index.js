import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { NavLink, Redirect, useHistory } from 'react-router-dom';
import { createNewBusiness } from '../../store/business';

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
    const [error, setError] = useState('')
    const [name, setName] = useState('')
    const [address, setAddress] = useState('')
    const [city, setCity] = useState('')
    const [state, setState] = useState('')
    const [zip, setZip] = useState('')
    const [price, setPrice] = useState('')
    const [phone, setPhone] = useState('')
    const [type, setType] = useState('')
    const [mon, setMon] = useState('')
    const [tue, setTue] = useState('')
    const [wed, setWed] = useState('')
    const [thu, setThu] = useState('')
    const [fri, setFri] = useState('')
    const [sat, setSat] = useState('')
    const [sun, setSun] = useState('')
    const [monClose, setMonClose] = useState('')
    const [tueClose, setTueClose] = useState('')
    const [wedClose, setWedClose] = useState('')
    const [thuClose, setThuClose] = useState('')
    const [friClose, setFriClose] = useState('')
    const [satClose, setSatClose] = useState('')
    const [sunClose, setSunClose] = useState('')
    const [site, setSite] = useState('')

    // useEffect(() => {
    //     const errors = []
    //     if (!site.includes('.com' || 'https:')) errors.push("Please enter a valid web address.")
    //     setError(errors)
    // }, [site])

    const handleSubmit = async (e) => {
        e.preventDefault()
        const data = {
            name, address, city, state, zip, price, phone, type,
            mon, tue, wed, thu, fri, sat, sun, site
        }
        const business = await dispatch(createNewBusiness(data)).catch(
            async (res) => {
                const businessData = await res.json();
                if (businessData && business.error) setError(data.error)
            }
        )
        if (business) history.push(`/business/${business.id}`)
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                {error.length > 0 && error.map((error, idx) => <li id="errormessages" key={idx}>{error}</li>)}
                <div>
                    <input type="text"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        placeholder="Name"
                    ></input>
                </div>
                <div>
                    <input type="text"
                        value={address}
                        onChange={(e) => setAddress(e.target.value)}
                        placeholder="Address"
                    ></input>
                </div>
                <div>
                    <input type="text"
                        value={city}
                        onChange={(e) => setCity(e.target.value)}
                        placeholder="City"
                    ></input>
                </div>
                <div>
                    <select type="text"
                        value={state}
                        onChange={(e) => setState(e.target.value)}>
                        {states.map(state => (<option value={state}>{state}</option>))}
                    </select>
                </div>
                <div>
                    <input type="text"
                        value={zip}
                        onChange={(e) => setZip(e.target.value)}
                        placeholder="Zip code"
                    ></input>
                </div>
                <div>
                    <select type="text"
                        value={price}
                        onChange={(e) => setPrice(e.target.value)}>
                        {priceOption.map(price => (<option value={price}>{price}</option>))}
                    </select>
                </div>
                <div>
                    <input type="text"
                        value={phone}
                        onChange={(e) => setPhone(e.target.value)}
                        placeholder="Phone number"
                    ></input>
                </div>
                <div>
                    <input type="text"
                        value={type}
                        onChange={(e) => setType(e.target.value)}
                        placeholder="Business type"
                    ></input>
                </div>
                <div>
                    <select type="text"
                        value={mon}
                        onChange={(e) => setMon(e.target.value)}>
                        {hours.map(hour => (<option value={hour}>{hour}</option>))}
                    </select>
                    <select type="text"
                        value={monClose}
                        onChange={(e) => setMonClose(e.target.value)}>
                        {hours.map(hour => (<option value={hour}>{hour}</option>))}
                    </select>
                </div>
                <div>
                    <select type="text"
                        value={tue}
                        onChange={(e) => setTue(e.target.value)}>
                        {hours.map(hour => (<option value={hour}>{hour}</option>))}
                    </select>
                    <select type="text"
                        value={tueClose}
                        onChange={(e) => setTueClose(e.target.value)}>
                        {hours.map(hour => (<option value={hour}>{hour}</option>))}
                    </select>
                </div>
                <div>
                    <select type="text"
                        value={wed}
                        onChange={(e) => setWed(e.target.value)}>
                        {hours.map(hour => (<option value={hour}>{hour}</option>))}
                    </select>
                    <select type="text"
                        value={wedClose}
                        onChange={(e) => setWedClose(e.target.value)}>
                        {hours.map(hour => (<option value={hour}>{hour}</option>))}
                    </select>
                </div>
                <div>
                    <select type="text"
                        value={thu}
                        onChange={(e) => setThu(e.target.value)}>
                        {hours.map(hour => (<option value={hour}>{hour}</option>))}
                    </select>
                    <select type="text"
                        value={thuClose}
                        onChange={(e) => setThuClose(e.target.value)}>
                        {hours.map(hour => (<option value={hour}>{hour}</option>))}
                    </select>
                </div>
                <div>
                    <select type="text"
                        value={fri}
                        onChange={(e) => setFri(e.target.value)}>
                        {hours.map(hour => (<option value={hour}>{hour}</option>))}
                    </select>
                    <select type="text"
                        value={friClose}
                        onChange={(e) => setFriClose(e.target.value)}>
                        {hours.map(hour => (<option value={hour}>{hour}</option>))}
                    </select>
                </div>
                <div>
                    <select type="text"
                        value={sat}
                        onChange={(e) => setSat(e.target.value)}>
                        {hours.map(hour => (<option value={hour}>{hour}</option>))}
                    </select>
                    <select type="text"
                        value={satClose}
                        onChange={(e) => setSatClose(e.target.value)}>
                        {hours.map(hour => (<option value={hour}>{hour}</option>))}
                    </select>
                </div>
                <div>
                    <select type="text"
                        value={sun}
                        onChange={(e) => setSun(e.target.value)}>
                        {hours.map(hour => (<option value={hour}>{hour}</option>))}
                    </select>
                    <select type="text"
                        value={sunClose}
                        onChange={(e) => setSunClose(e.target.value)}>
                        {hours.map(hour => (<option value={hour}>{hour}</option>))}
                    </select>
                </div>
                <div>
                    <input type="text"
                        value={site}
                        onChange={(e) => setSite(e.target.value)}
                        placeholder="Your site"
                    ></input>
                </div>
            </form>
        </div>
    )

}


export default EditBusinessForm;
